<p align="center">
  <img src="https://i.imgur.com/xj0pSxA.png" width="100%" />
</p>

<h1 align="center">🔐 USB DRIVE AUTHENTICATION SYSTEM</h1>
<h3 align="center">Turn Your USB Pen-Drive Into a Physical Security Key 🔑💻🛡️</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Windows-10/11-lightgrey?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Security-High-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Automation-Active-blue?style=for-the-badge" />
</p>

---

## 🚀 Overview  
This project converts your **USB flash drive** into a **hardware authentication key**.

- 🟢 USB inserted → System stays unlocked  
- 🔴 USB removed → ⚠️ Instantly logs off Windows  

💡 Works exactly like a **car key**:  
Remove the key → engine stops.  
Remove USB → system locks. 🚗💨  

---

## 🌟 Why This Is Useful  
- ✔ Prevent unauthorized access  
- ✔ Perfect for office, hostel, shared PCs  
- ✔ Lightweight & fast  
- ✔ No external software needed  
- ✔ Runs silently in background  
- ✔ Uses unspoofable **USB hardware serial**  
- ✔ AMAZING interview project (security + OS + automation + Python)

> 🔐 Passwords can leak.  
> Hardware serials are MUCH harder to fake.

---

## 🧠 How It Works (High-Level)

### 🔌 1️⃣ USB Serial Extraction  
Using WMIC:  
wmic diskdrive get serialnumber

### 🧠 2️⃣ Python Script Monitors USB  
Every few seconds script checks:

- If serial exists → 🟢 continue  
- If not → 🔴 log off  

### ⚡ 3️⃣ Auto Security  
No human interaction needed → full automation.

---

## 🧩 Core Concepts (Quick Revision)

| 🔢 Concept       | 🧠 Meaning                                                   |
|------------------|-------------------------------------------------------------|
| 🔌 USB Serial    | Unique hardware ID for your pen-drive                       |
| 🧠 Python Script | Monitors system continuously                                 |
| 📝 WMIC          | Windows tool to fetch hardware info                          |
| 🗂 Temp File     | Stores WMIC output temporarily                               |
| 🔁 Loop          | Checks USB presence every few seconds                        |
| ⚡ Auto Logoff   | Logs off instantly when USB is removed                       |

---

## 📁 Project Structure

USB-drive-authentication/
├── USB.py # Main authentication script
├── README.md # Documentation
└── .gitignore # Ignore temporary files


---

## 🧾 Main Script (USB.py)

```python
import os
import time

# Set your authorized USB serial number
TARGET_SERIAL = "YOUR_SERIAL_HERE"

while True:
    # Wait for 10 seconds before each check
    time.sleep(10)

    # Get serial numbers of connected USB disks
    os.system("wmic diskdrive get serialnumber > usblist.txt")

    try:
        # Read WMIC output
        with open("usblist.txt", "r", encoding="utf-16le") as file:
            content = file.read()

        os.remove("usblist.txt")

        # If authorized USB is not found → log off
        if TARGET_SERIAL not in content:
            os.system("shutdown -l")
            break

    except Exception:
        time.sleep(10)

🔍 How to Get Your USB Serial Number
Run this command in CMD:

arduino
Copy code
wmic diskdrive get serialnumber
Example Output:

nginx
Copy code
SerialNumber
037D13C1ABC0
59A8F903XYZ1
Replace in script:

python
Copy code
TARGET_SERIAL = "037D13C1ABC0"

⚙️ Setup & Run
1️⃣ Requirements

🪟 Windows 10/11

🐍 Python 3.x

Any USB flash drive

2️⃣ Clone the Repo
git clone https://github.com/Yogesh0311/USB-drive-autintication-.git
cd USB-drive-autintication-

3️⃣ Configure Serial

Update inside USB.py:

TARGET_SERIAL = "YOUR_SERIAL"

4️⃣ Run Script
python USB.py


🟢 Keep USB inserted
🔴 Remove USB → instant logoff

🚀 Auto-Run on Windows Startup
✔ Method 1 (Recommended) – Task Scheduler

Open:

taskschd.msc


Create task:

Trigger → At log on

Action → Start program (python USB.py)

Run with highest privileges → ✔

Save

✔ Method 2 – Startup Folder

Paste shortcut here:

%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

🔒 .gitignore (Important)
usblist.txt
*.log
__pycache__/
*.pyc
*.exe


⚠️ Never push your real USB Serial to GitHub!

📊 Useful Commands
Command	Purpose
wmic diskdrive get serialnumber	Get USB serial
python USB.py	Run script
shutdown -l	Log off user
taskschd.msc	Open Task Scheduler
git status	Check changes
git add .	Stage all changes
git commit -m "message"	Commit changes
git push origin main	Push to GitHub