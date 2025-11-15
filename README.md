🔐 USB Drive Authentication Guide

Your physical security key for Windows 💻🔑

🌱 What Is This?

A lightweight Python + Windows script that uses a USB drive as a physical authentication token.

If the correct USB is not connected →
💥 Your Windows session logs off instantly.

Think of it like a security key — the system stays open only as long as your USB is inserted.

🔧 How It Works

Every USB drive has a unique serial number.

Script checks every few seconds if that serial exists.

If not found →

shutdown -l


→ system logs off.

🧠 Core Concepts (Visual Summary)
🌟 Feature	🔍 Description
🔌 USB Serial	Unique ID used as authentication
📝 WMIC	Reads USB serial numbers from Windows
🧠 Python Script	Monitors and compares serials
⚡ Auto Logoff	Logs out when unauthorized USB is detected
📂 Temp File	Used to store WMIC output briefly
🔁 Loop	Checks USB every X seconds
🛠️ Project Structure
usb-auth/
├── usb_auth.py        # Main authentication script
├── README.md          # This guide
└── .gitignore         # Ignore temp + sensitive files

📄 Core Script Example
import os
import time

TARGET_SERIAL = "037D13C130C0"  # Your USB serial

while True:
    time.sleep(10)
    os.system("wmic diskdrive get serialnumber > usblist.txt")

    try:
        with open("usblist.txt", "r", encoding="utf-16le") as f:
            content = f.read()

        os.remove("usblist.txt")

        if TARGET_SERIAL not in content:
            os.system("shutdown -l")
            break

    except Exception:
        time.sleep(10)

🧪 How to Get Your USB Serial Number

Run this in Command Prompt:

wmic diskdrive get serialnumber


Pick the serial ID of your USB → put into TARGET_SERIAL.

💻 Example Output (WMIC)
SerialNumber
037D13C130C0
WD-WX52A1234567

🔐 Auto-Start on Windows (Optional)
Option 1 — Task Scheduler

✔️ Best method
✔️ Auto-runs with admin privileges

Option 2 — Startup Folder

Quick but less secure.

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup


Place a shortcut to the script here.

🔒 .gitignore (Important!)
usblist.txt
*.log
*.exe
__pycache__/


🙅 Never upload your USB serial to GitHub if it's a sensitive environment.

📊 Command Summary
🔧 Command	💡 What It Does
wmic diskdrive get serialnumber	Fetch USB serial number
shutdown -l	Logs off user
python usb_auth.py	Runs script
taskschd.msc	Opens Task Scheduler
🚀 GitHub Upload
git init
git add .
git commit -m "USB authentication system"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main

🧠 Pro Tips

Keep your USB physically safe — it is the key.

Use a known, reliable, no-loose-port USB drive.

Convert script to EXE for better security using PyInstaller.

Use Task Scheduler to prevent users from bypassing the script.

📚 Helpful Links

📘 Python Docs
🌐 WMIC Reference
🔐 Windows Security Commands
