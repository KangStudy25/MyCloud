# 📂 MyCloud - Personal Cloud Storage

Cloud pribadi sederhana untuk mengelola file antar perangkat.

## 🚀 Cara Install Cepat
Cukup jalankan perintah ini di Termux atau Terminal Linux:

```bash
git clone https://github.com/KangStudy25/MyCloud.git && cd mycloud && chmod +x install.sh && ./install.sh

```
# NOTE

## 🛠️PENGATURAN JALUR PENYIMPANAN (MANUAL PATH)

Masukkan jalur folder tempat file akan disimpan di bawah ini.

CONTOH PENGISIAN JALUR:
 - SD Card: "/storage/0625-F3EF/Android/media/com.termux/CloudKu"
 - Internal: "/storage/emulated/0/Android/media/com.termux/CloudKu"
 - Windows: "C:/Users/NamaPC/Downloads/CloudKu"

Buka file app. py, atur bagian:
```
MANUAL_PATH = "/storage/0625-F3EF/Android/media/com.termux/CloudKu"
```
### Pengaturan Port

Kode printah

Contoh: python app.py port-yang-diinginkan>
```
python app.py 7060
```


# 📂 MyCloud + Client Cloud (Gunakan folder Server_Client)

Cloud pribadi + agent uploud otomatis di perangkat yang berbeda.

## 🚀 Cara Install Cepat
Cukup jalankan perintah ini di Termux atau Terminal Linux:

```bash
git clone https://github.com/KangStudy25/MyCloud.git && cd mycloud/Server_Client && chmod +x install.sh && ./install.sh
```
# NOTE

## 🛠️PENGATURAN JALUR PENYIMPANAN (MANUAL PATH)

Masukkan jalur folder tempat file akan disimpan di bawah ini.

CONTOH PENGISIAN JALUR:
 - SD Card: "/storage/0625-F3EF/Android/media/com.termux/CloudKu"
 - Internal: "/storage/emulated/0/Android/media/com.termux/CloudKu"
 - Windows: "C:/Users/NamaPC/Downloads/CloudKu"

Buka file app. py, atur bagian:
```
MANUAL_PATH = "/storage/0625-F3EF/Android/media/com.termux/CloudKu"
```
## Kunci Keamanan agar hanya Agent Kakak yang bisa upload
```SYNC_TOKEN = "KunciRahasiaCloud123"``` ## Kunci agar Server dan Agent dapat berkomunikasi (Dapat Dirubah Harus sama antara Agen dan MyCloud)

### Pengaturan Port

Kode printah

Contoh: python app.py port-yang-diinginkan>
```
python app.py 7060
```
## 🛠️PENGATURAN JALUR dan IP PADA AGENT

```SERVER_IP = "10.136.92.30"``` ### Ganti dengan IP Server MyCloud

```SERVER_URL = f"http://10.136.92.30:5000/api/sync"``` ### Gunakan URL server

```WATCH_PATH = r"E:\Agen"``` ### Folder yang menjadi tempat penyimpanan yang ingin di backup secara otomatis di MyCloud

```TOKEN = "KunciRahasiaCloud123"``` ### Kunci agar Server dan Agent dapat berkomunikasi (Dapat Dirubah Harus sama antara Agen dan MyCloud)

