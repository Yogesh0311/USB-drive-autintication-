# USB Drive Authentication System

A lightweight Python-based security system that uses USB drive serial number verification to control user access on Windows computers.

## 📋 Overview

This project implements a hardware-based authentication mechanism that continuously monitors for the presence of a specific USB device. If the authorized USB drive is removed or not detected, the system automatically logs off the user, preventing unauthorized access.

## ✨ Features

- **Physical Authentication**: Uses unique USB serial numbers as hardware keys
- **Automatic Monitoring**: Continuously checks USB presence every 10 seconds
- **Instant Response**: Triggers immediate logoff when authorized USB is removed
- **Lightweight**: Minimal system resource consumption
- **No Additional Hardware**: Works with any standard USB drive
- **Simple Setup**: Easy configuration and deployment

## 🔧 System Requirements

| Component | Requirement |
|-----------|-------------|
| Operating System | Windows 10/11 (64-bit) |
| Python Version | 3.8 or higher |
| Privileges | Administrator rights required |
| USB Device | Any standard USB 2.0/3.0 drive |
| Storage | At least 100 MB free disk space |

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/usb-drive-authentication.git
cd usb-drive-authentication
```

2. **Install Python** (if not already installed)
   - Download from [python.org](https://www.python.org)
   - Ensure "Add Python to PATH" is checked during installation

3. **Verify WMIC availability** (built-in on Windows)
```cmd
wmic diskdrive get serialnumber
```

## 📝 Configuration

1. **Find your USB serial number**
```cmd
wmic diskdrive get serialnumber
```

2. **Edit the script**
Open `usb_auth.py` and update the `TARGET_SERIAL` variable:
```python
TARGET_SERIAL = "YOUR_USB_SERIAL_NUMBER"
```

## 🎯 Usage

### Basic Usage
Run the script with administrator privileges:
```cmd
python usb_auth.py
```

### Auto-start on System Boot

**Method 1: Task Scheduler**
1. Open Task Scheduler (`Win + R` → `taskschd.msc`)
2. Create a new task
3. Set trigger to "At log on"
4. Set action to start `usb_auth.py`
5. Enable "Run with highest privileges"

**Method 2: Startup Folder**
Place a shortcut in:
```
C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

## 💻 Code Example
```python
import os
import time

TARGET_SERIAL = "037D13C2140"

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
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
```

## 🎓 Use Cases

- **Personal Computers**: Protect sensitive data with physical authentication
- **Office Environments**: Ensure only authorized personnel access workstations
- **Educational Institutions**: Control USB usage in computer labs
- **Public Terminals**: Prevent unauthorized access in shared spaces
- **Parental Control**: Monitor and restrict system access

## ⚙️ How It Works

1. **Detection**: Script queries Windows for connected USB devices using WMIC
2. **Verification**: Compares detected serial numbers against authorized serial
3. **Action**: If match found, continues monitoring; if not, triggers user logoff
4. **Loop**: Repeats check every 10 seconds

## 🔒 Security Features

- Hardware-based physical authentication
- Unique device identification via serial numbers
- Automatic session termination on unauthorized access
- No password dependency
- Temporary file cleanup for data security

## ⚠️ Limitations

- Windows-only (WMIC dependency)
- Single authorized device in current version
- Vulnerable to advanced serial number spoofing
- No data encryption (access control only)
- Requires manual setup
- No pre-logoff warnings

## 🛠️ Troubleshooting

**Script doesn't trigger logoff**
- Ensure running with administrator privileges
- Verify WMIC is available on your system

**USB not detected**
- Check USB connection and mounting
- Wait 10-15 seconds for detection cycle

**Permission errors**
- Right-click → "Run as Administrator"

## 🚧 Future Enhancements

- [ ] Multi-device whitelist support
- [ ] Cross-platform compatibility (Linux/macOS)
- [ ] GUI interface for easier configuration
- [ ] Encryption integration
- [ ] Pre-logoff warning notifications
- [ ] Cloud-based device management
- [ ] Activity logging and audit trails

## 📚 Documentation

For detailed documentation, see:
- [User Manual](docs/USER_MANUAL.md)
- [Developer Guide](docs/DEVELOPER_GUIDE.md)
- [API Reference](docs/API_REFERENCE.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Yogesh** -  BTECh Final Year Project



## 📧 Contact

For questions or support, please open an issue in the GitHub repository.



## ⚖️ Disclaimer

This software is provided for educational and research purposes. Users are responsible for ensuring compliance with organizational policies and local regulations regarding system security and access control.

---

**Note**: Always maintain a backup method of system access in case of USB device failure or loss.
