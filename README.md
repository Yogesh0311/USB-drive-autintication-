🔐 USB DRIVE AUTHENTICATION SYSTEM
Your USB Pen-Drive Becomes a Physical Security Key 🔑💻🛡️
🌟 What Is This?

This project turns your USB flash drive into a hardware-level login key.

When your USB is connected → your system stays unlocked

Remove it → ⚠️ Instant Windows Logoff

It’s like a digital car key → pull it out, engine stops. 🚗💨
Same for your PC.

💡 Why Use It?

✔️ Prevent unauthorized system access
✔️ Perfect for shared/home/office PCs
✔️ Lightweight and fast
✔️ Zero third-party tools
✔️ No GUI needed
✔️ Runs silently in background

Passwords can leak.
Your USB hardware signature cannot.

⚙️ How It Works (Super Simple)
🔌 Step 1 — Unique USB Serial

Every USB has a unique serial number (fetched using WMIC).

🧠 Step 2 — Python Script Monitors Serial

If serial matches → ✔️ continue

If not → ❌ logoff instantly

⚡ Step 3 — Auto Protection

No human interaction needed.

🧠 Core Concepts (Visual Summary)
Icon	Feature	Description
🔌	USB Serial	Unique ID used for authentication
🧠	Python Script	Core logic running continuously
📝	WMIC Tool	Reads USB info from Windows
⚡	Auto Logoff	Logs user out if key is missing
🗂️	Temp File	Stores WMIC output briefly
🔁	Monitoring Loop	Repeats every 10 seconds
📁 Project Structure
usb-auth/
├── usb_auth.py        # Main authentication script
├── README.md          # Documentation
└── .gitignore         # Prevents sensitive files from being pushed

📄 Full Script (Optimized & Clean)
import os
import time

# Set your authorized USB serial number
TARGET_SERIAL = "037D13C130C0"

while True:
    time.sleep(10)
    os.system("wmic diskdrive get serialnumber > usblist.txt")

    try:
        with open("usblist.txt", "r", encoding="utf-16le") as file:
            content = file.read()

        os.remove("usblist.txt")

        if TARGET_SERIAL not in content:
            os.system("shutdown -l")
            break

    except Exception:
        time.sleep(10)

🔍 How to Get Your USB Serial Number

Run this in CMD:

wmic diskdrive get serialnumber

Example Output:
SerialNumber
037D13C130C0
WD-WX52A9988123


Then set:

TARGET_SERIAL = "YOUR_SERIAL_HERE"

🚀 Auto-Start on Windows (Auto Protection)
✔️ Method 1 — Task Scheduler (Recommended)

Runs script at system login

Hidden from normal users

Works even after reboot

✔️ Method 2 — Startup Folder (Quick)

Paste a shortcut in:

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

🔒 .gitignore (Required)
usblist.txt
*.log
__pycache__/
*.exe
*.pyc


Never upload your USB serial publicly.

📊 Useful Commands
Command	Purpose
wmic diskdrive get serialnumber	Fetch USB serial
python usb_auth.py	Start script
shutdown -l	Log off user
taskschd.msc	Open Task Scheduler
🧠 Pro Security Tips

🔥 Convert script into .exe with PyInstaller
🔥 Hide task in Task Scheduler
🔥 Add multiple serials for multi-user authentication
🔥 Add pop-ups before logoff (optional enhancement)
🔥 Combine with disk encryption for maximum protection

🌍 Push to GitHub
git init
git add .
git commit -m "USB Authentication System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
