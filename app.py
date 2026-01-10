import os
import time
import shutil
import zipfile
import io
from flask import Flask, render_template, request, redirect, send_from_directory, url_for, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ====================================================================
#Menetapkan Jalut PATH Secara Manual
MANUAL_PATH = "..."
# ====================================================================

def get_upload_path():
    if MANUAL_PATH and os.path.exists(MANUAL_PATH):
        return MANUAL_PATH

UPLOAD_FOLDER = get_upload_path()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
print(f"\n[INFO] MyCloud aktif menggunakan lokasi: {UPLOAD_FOLDER}\n")

CATEGORIES = {
    'Gambar': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff', 'svg'],
    'Video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'flv'],
    'Audio': ['mp3', 'wav', 'aac', 'm4a', 'ogg', 'flac', 'm4a'],
    'Dokumen': ['docx', 'pdf', 'txt', 'xlsx', 'pptx', 'csv', 'xls', 'rtf', 'doc']
}

def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} Bytes"
    elif size_bytes < 1024**2:
        return f"{round(size_bytes / 1024, 2)} KB"
    elif size_bytes < 1024**3:
        return f"{round(size_bytes / (1024**2), 2)} MB"
    else:
        return f"{round(size_bytes / (1024**3), 2)} GB"

def get_file_info(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(path): return None
    stat = os.stat(path)
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    cat_found = 'Lainnya'
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            cat_found = category
            break
    return {
        'name': filename,
        'display_name': filename.replace('-', ' '),
        'size_mb': stat.st_size / (1024 * 1024),
        'size_str': format_size(stat.st_size),
        'time': time.strftime('%d/%m/%Y %H:%M', time.localtime(stat.st_mtime)),
        'raw_time': stat.st_mtime,
        'category': cat_found
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')
        for file in files:
            if file.filename != '':
                clean_name = secure_filename(file.filename).replace(' ', '-')
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], clean_name))
        return "OK", 200

    all_files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_infos = [get_file_info(f) for f in all_files if get_file_info(f)]
    file_infos.sort(key=lambda x: x['raw_time'], reverse=True)

    stats_raw = {cat: 0 for cat in CATEGORIES.keys()}
    stats_raw['Lainnya'] = 0
    grouped_files = {cat: [] for cat in CATEGORIES.keys()}
    grouped_files['Lainnya'] = []

    for info in file_infos:
        grouped_files[info['category']].append(info)
        stats_raw[info['category']] += info['size_mb']

    formatted_stats = {}
    for cat, mb in stats_raw.items():
        formatted_stats[cat] = format_size(int(mb * 1024 * 1024))

    # PERBAIKAN: Cek storage pada path SD Card
    total, used, free = shutil.disk_usage(UPLOAD_FOLDER)
    storage = {'total': round(total/(1024**3),1), 'used': round(used/(1024**3),1),
               'free': round(free/(1024**3),1), 'percent': round((used/total)*100,1)}

    return render_template('index.html', grouped_files=grouped_files, storage=storage, stats=formatted_stats)

@app.route('/download-zip', methods=['POST'])
def download_zip():
    filenames = request.json.get('filenames', [])
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for fname in filenames:
            path = os.path.join(app.config['UPLOAD_FOLDER'], fname)
            if os.path.exists(path):
                zf.write(path, fname)
    memory_file.seek(0)
    return send_file(memory_file, download_name="Cloud_Files.zip", as_attachment=True)

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<path:filename>')
def delete_file(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(path): os.remove(path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    import sys
    port = 5000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
