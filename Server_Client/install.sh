#!/bin/bash
echo "Menyiapkan MyCloud..."

# Cek sistem (Termux vs Linux/PC)
if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    pkg update && pkg upgrade -y
    pkg install python git -y
    termux-setup-storage
else
    sudo apt update
    sudo apt install python3 python3-pip git -y
fi

# Install Flask & Werkzeug
pip install flask werkzeug

# Untuk agen
pip install watchdog requests

echo "Instalasi selesai! Jalankan dengan: python app.py"
