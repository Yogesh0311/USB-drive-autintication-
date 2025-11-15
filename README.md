USB Drive Authentication System

A lightweight security system that locks/logs off a Windows PC if a specific USB drive (based on serial number) is removed.
The USB drive acts as a physical authentication token — a “key” — and without it, the system forces logoff.

This project uses:

Python

WMIC (Windows Management Instrumentation Command-line)

Windows logoff command

Works on Windows 10/11.
Designed to be simple, minimal, and effective.

🔐 How It Works

Every USB drive has a unique Serial Number.

The script continuously checks if the authorized USB (with that serial) is connected.

If the serial is not detected, the system immediately executes:

shutdown -l


→ Logging off the active Windows user.

🧠 Features

Hardware-based authentication (cannot be bypassed with passwords)

Lightweight Python script

No external libraries

Continuous background monitoring

Auto logoff on unauthorized usage

No installation required

🗂️ Project Structure
│
├── usb_auth.py          # Main Python script
├── README.md            # Documentation
└── (temporary) usblist.txt    # Auto-created & deleted during runtime

⚙️ Requirements
Hardware

Any USB Flash Drive (used as the “key”)

Windows PC (Win10/Win11)

Software

Python 3.6+

WMIC (pre-installed in Windows)

Administrator privileges (required for logoff)

🛠️ Setup Instructions
1. Get Your USB Serial Number

Open Command Prompt and run:

wmic diskdrive get serialnumber


Note down the serial of the USB you want to authorize.

2. Set Your Serial in the Script

Open usb_auth.py and update:

TARGET_SERIAL = "PUT-YOUR-USB-SERIAL-HERE"


Example:

TARGET_SERIAL = "037D13C130C0"

3. Run the Script

Open Command Prompt (Run as Administrator):

python usb_auth.py


The script will now check every 10 seconds for your USB.
If the USB is removed → User is logged off immediately.

🧪 How the Script Works (Code Overview)
import os
import time

TARGET_SERIAL = "037D13C130C0"

while True:
    time.sleep(10)
    os.system("wmic diskdrive get serialnumber > usblist.txt")

    try:
        with open("usblist.txt", "r", encoding="utf-16le") as readfile:
            content = readfile.read()

        os.remove("usblist.txt")

        if TARGET_SERIAL not in content:
            os.system("shutdown -l")
            break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)

🧩 How to Run at System Startup (Optional)
Option A: Task Scheduler (recommended)

Open Task Scheduler

Create New Task

Trigger: At logon

Action: Start program

Program: python.exe

Arguments: C:\path\usb_auth.py

Enable Run with highest privileges

Option B: Startup Folder

Place a shortcut here:

C:\Users\<Username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

⚠️ Limitations

Works only on Windows (WMIC-based)

WMIC is deprecated in latest Win11 builds (switch to PowerShell in future)

Serial numbers can technically be spoofed (not trivial)

No warning before logoff — it’s immediate

No encryption or multi-device support in base version

🚀 Future Enhancements

PowerShell-based USB detection (modern Windows)

Support multiple authorized USBs

Encrypted config file

GUI interface for configuration

Pop-up warning before forced logoff

📄 License

Open-source. Do whatever you want with it.
