# 🔐 USB DRIVE AUTHENTICATION SYSTEM  
Turn Your USB Pen-Drive Into a Physical Security Key 🔑💻🛡️  

---

## 🚀 Overview

This project turns your **USB flash drive** into a **hardware security key**.

- ✅ USB inserted → System stays unlocked  
- ❌ USB removed → ⚠️ Instant **Windows Logoff**

Think of it like a **car key**:  
Pull the key out → engine stops.  
Remove the USB → session ends. 🚗💨

---

## 🌟 Why This Is Useful

- ✔ Prevent **unauthorized access** to your PC  
- ✔ Great for **shared PCs / hostel / office systems**  
- ✔ Lightweight **Python script**, no heavy tools  
- ✔ Runs silently in the **background**  
- ✔ Uses your USB’s **unique hardware serial**  
- ✔ Perfect for **explaining in interviews** (security + automation + OS + Python)

> 💡 Passwords can leak.  
> A physical USB serial is much harder to fake for normal users.

---

## 🧠 How It Works (High-Level)

1. **Get USB Serial Number**  
   - Use a WMIC command to read the **unique serial number** of your USB drive.

2. **Python Script Monitors USB**  
   - Every **few seconds** the script checks:  
     - If authorized serial is found → ✅ do nothing  
     - If not found → ❌ instantly log off current user

3. **Auto Security**  
   - As soon as someone removes your USB → session is terminated.

---

## 🧩 Core Concepts (Quick Revision)

| 🔢 Concept       | 🧠 What It Means                                       |
|------------------|--------------------------------------------------------|
| 🔌 USB Serial    | Unique ID of your USB, used as authentication token    |
| 🧠 Python Script | Main logic that continuously monitors the system       |
| 📝 WMIC          | Windows tool to read hardware info (like disk serial)  |
| 🗂 Temp File     | Stores WMIC output temporarily (`usblist.txt`)         |
| 🔁 Monitoring    | Infinite loop that checks every X seconds              |
| ⚡ Auto Logoff   | Logs off user if USB key is missing                    |

This is a **great DSA + OS + Security** discussion point in interviews.

---

## 📁 Project Structure

```bash
USB-drive-authentication/
├── USB.py        # Main authentication script
├── README.md     # Project documentation
└── .gitignore    # Ignore temporary/sensitive files

##🧾 Main Script (USB.py)
import os
import time

# Set your authorized USB serial number (replace with your actual serial)
TARGET_SERIAL = "YOUR_SERIAL_HERE"

while True:
    # Wait for 10 seconds before each check
    time.sleep(10)

    # Get serial numbers of connected disk drives
    os.system("wmic diskdrive get serialnumber > usblist.txt")

    try:
        # Read WMIC output (UTF-16 LE encoding)
        with open("usblist.txt", "r", encoding="utf-16le") as file:
            content = file.read()

        # Remove temporary file
        os.remove("usblist.txt")

        # If our authorized USB serial is NOT found → log off user
        if TARGET_SERIAL not in content:
            os.system("shutdown -l")
            break

    except Exception:
        # On any error, wait and retry
        time.sleep(10)

##🔍 How to Get Your USB Serial Number

Plug in your USB drive.

Open Command Prompt (CMD) on Windows.

Run:  wmic diskdrive get serialnumber

Example output:

SerialNumber
037D13C1nnn
59A8F903nnn


Take your USB’s actual serial (e.g. 037D13C130C0) and set:

TARGET_SERIAL = "037D13nnn"

##  ⚙️ Setup & Run
1️⃣ Requirements

🪟 Windows 10 / 11

🐍 Python 3.x installed and in PATH

Any normal USB flash drive

##  2️⃣ Clone or Download

If using Git:

git clone https://github.com/Yogesh0311/USB-drive-autintication-.git
cd USB-drive-autintication-

##  3️⃣ Configure Your Serial

Edit USB.py:

TARGET_SERIAL = "YOUR_REAL_USB_SERIAL_HERE"

##  4️⃣ Run the Script
python USB.py


Keep your USB inserted while working

Remove USB → system logs off ⚠️

##  🚀 Auto-Run on Windows Startup
✅ Method 1 – Task Scheduler (Recommended)

Open Task Scheduler

taskschd.msc


Create New Task:

Trigger: At log on

Action: Start program → python with argument C:\path\to\USB.py

Check “Run with highest privileges”

Save it.

Now the script runs automatically whenever you log in.

✅ Method 2 – Startup Folder (Simple)

Create a shortcut to USB.py or a .bat file that runs it.

Paste the shortcut here:

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup


On next login, Windows will auto-run it.

 ## 🔒 .gitignore (Important for GitHub)

Make sure your repo has this:

usblist.txt
*.log
__pycache__/
*.pyc
*.exe


⚠️ Never upload your real USB serial or any sensitive info to public repos.

##  📊 Useful Commands (Quick Table)
| 🧾 Command                        | 💡 Purpose              |
| --------------------------------- | ----------------------- |
| `wmic diskdrive get serialnumber` | Get USB serial numbers  |
| `python USB.py`                   | Run the script          |
| `shutdown -l`                     | Log off current user    |
| `taskschd.msc`                    | Open Task Scheduler GUI |
| `git status`                      | Check Git changes       |
| `git add .`                       | Stage all changes       |
| `git commit -m "message"`         | Commit changes          |
| `git push origin main`            | Push to GitHub          |
