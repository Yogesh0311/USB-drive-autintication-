🔐 USB DRIVE AUTHENTICATION SYSTEM
Turn Your USB Pen-Drive Into a Physical Security Key 🔑💻🛡️
🌟 What Is This?

A Python-based security tool that uses your USB drive’s unique serial number as a hardware authentication key.

USB inserted → System stays unlocked

USB removed → ⚠️ Instant Windows Logoff

Exactly like a car key → pull it out, engine shuts off. 🚗💨

💡 Why Use It?

✔ Prevent unauthorized access
✔ Protect sensitive work
✔ Works on any Windows system
✔ Runs silently in background
✔ No external tools needed
✔ Lightweight & fast

Your password can leak.
Your USB’s hardware serial cannot.

⚙️ How It Works
🔌 1. Find USB Serial

WMIC command extracts the USB’s unique ID.

🧠 2. Script Checks Continuously

Every 10 seconds the script checks:

If serial matches → Normal operation

If serial missing → Logoff

⚡ 3. Auto Security

Lock happens automatically.

🧠 Core Concepts
Icon	Feature	Description
🔌	USB Serial	Unique ID used for authentication
🧠	Python Script	Runs the monitoring logic
📝	WMIC	Command to read USB info
⚡	Auto Logoff	Logs user out if key missing
🗂	Temp File	Stores WMIC output
🔁	Loop	Repeats every few seconds
📁 Project Structure
USB-drive-authentication/
├── USB.py              # Main authentication script
├── README.md           # Documentation
└── .gitignore          # Ignore sensitive files

📄 Full Script (USB.py)
import os
import time

# Set your authorized USB serial number
TARGET_SERIAL = "YOUR_SERIAL_HERE"

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

Run this in Windows CMD:

wmic diskdrive get serialnumber


Example:

SerialNumber
037D13C130C0
59A8F9031234


Then put this serial here:

TARGET_SERIAL = "037D13C130C0"

🚀 Auto-Run on Windows Startup
✔ Task Scheduler (Recommended)

Run script at login

Hidden from normal users

Harder to bypass

✔ Startup Folder (Simple)

Paste shortcut here:

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

🔒 .gitignore (Required)
usblist.txt
*.log
__pycache__/
*.pyc
*.exe


Never upload real USB serial numbers publicly.

📊 Useful Commands
Command	Use
wmic diskdrive get serialnumber	Get USB serial
python USB.py	Run script
shutdown -l	Log off user
taskschd.msc	Open Task Scheduler