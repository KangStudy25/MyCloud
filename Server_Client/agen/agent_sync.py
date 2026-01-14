import time
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- KONFIGURASI SINKRONISASI ---
SERVER_IP = "10.136.92.30"  # Ganti dengan IP Server Kakak
SERVER_URL = f"http://10.136.92.30:5000/api/sync"
WATCH_PATH = r"E:\Agen"    # Folder di laptop yang dipantau
TOKEN = "KunciRahasiaCloud123"
# -------------------------------

class FlatSyncHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory: self.send_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory: self.send_file(event.src_path)

    def send_file(self, file_path):
        # Ambil nama filenya saja (Tanpa Folder)
        file_name = os.path.basename(file_path)
        print(f"[*] Terdeteksi perubahan: {file_name}")
        
        try:
            with open(file_path, 'rb') as f:
                response = requests.post(
                    SERVER_URL, 
                    files={'file': f}, 
                    data={'path': file_name}, 
                    headers={'Authorization': TOKEN}
                )
                if response.status_code == 200:
                    print(f"[OK] Berhasil Sync: {file_name}")
        except Exception as e:
            print(f"[!] Gagal mengirim {file_name}: {e}")

if __name__ == "__main__":
    if not os.path.exists(WATCH_PATH):
        os.makedirs(WATCH_PATH)
        
    observer = Observer()
    # recursive=True agar dia tetap mencari file di dalam sub-folder laptop
    observer.schedule(FlatSyncHandler(), WATCH_PATH, recursive=True)
    observer.start()
    print(f"Agent Aktif! Memantau {WATCH_PATH} (Berlapis) -> Server (Flat)")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()