🔐✨ USB Drive Authentication System
Your Personal Hardware Security Key for Windows 💻🔑⚡

Secure your PC the cool way — using a USB pen-drive as a physical login key.

Remove the USB → boom, instant logoff.
Plug it in → system stays unlocked.
Simple. Fast. Effective.

🌟 Why This Exists

Passwords can be leaked.
People can peek.
Software locks can be bypassed.

But your USB drive’s unique serial number?
That’s a physical identity — harder to fake, harder to bypass.

This project turns your USB drive into a real-world authentication token.

🚀 How It Works (Super Simple)

1️⃣ You register your USB’s serial number
2️⃣ The Python script keeps checking every few seconds
3️⃣ If the USB is missing → Windows logs off instantly
4️⃣ No chance for anyone to continue using your PC 🔒

🧠 Core Concepts (Visual Quick Guide)
🌟 Component	💡 What It Means
🔌 USB Serial	Unique identity of your USB device
📝 WMIC	Reads USB info from Windows
🧠 Python Script	Handles the monitoring logic
⚡ Auto-Logoff	Forces logoff if USB is removed
🗃️ Temp File	Stores WMIC output briefly
🔁 Loop	Keeps checking every 10 seconds
🛠️ Project Structure (Clean & Minimal)
usb-auth/
├── usb_auth.py        # Core authentication script
├── README.md          # This creative documentation
└── .gitignore         # Ignores sensitive files

📸 Demo Flow (Conceptual)

🔌 USB Inserted → System Active
🧠 Script detects: “Serial OK”
⏳ Keeps monitoring…

❌ USB Removed → Unauthorized
⚠️ Script detects: “Serial NOT FOUND”
💥 Instant Logoff Triggered

Just like pulling the key out of a car engine. 🚗💨

💾 Example Code (Clean & Commented)
import os
import time

# Your authorized USB serial number
TARGET_SERIAL = "037D13C130C0"

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

🧪 Get Your USB Serial Number

Run this in CMD:

wmic diskdrive get serialnumber


Copy your serial → paste into this line:

TARGET_SERIAL = "YOUR_SERIAL_HERE"


Done. That’s your physical key now 🔑.

🌍 Auto-Start on Windows (Optional but Recommended)
✔️ Task Scheduler (Best Method)

Run script at login

Run with admin privilege

Harder to bypass

⚡ Startup Folder

Quick & simple:

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup


Drop your script shortcut here.

🔒 .gitignore (Protect Yourself!)
usblist.txt
*.log
__pycache__/
*.exe


🙅 Never upload your serial number publicly.

📊 Helpful Commands
Command	Action
wmic diskdrive get serialnumber	Get USB serial
python usb_auth.py	Run the script
shutdown -l	Force logoff
taskschd.msc	Open Task Scheduler
🚀 Publish to GitHub
git init
git add .
git commit -m "USB Drive Authentication initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main

🧠 Pro Tips to Level-up

🔥 Turn script into .exe using PyInstaller
🔥 Hide script in Task Scheduler for stealth mode
🔥 Add multiple USBs for multi-key authentication
🔥 Add notifications or GUI (future upgrades)
