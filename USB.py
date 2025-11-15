import os
import time

TARGET_SERIAL = "0401546120255ac788e9"

while True:
    time.sleep(10)  # Pause for 30 seconds between checks

    # Get list of USB drive serial numbers
    os.system("wmic diskdrive get serialnumber > usblist.txt")

    try:
        with open("usblist.txt", "r", encoding="utf-16le") as readfile:
            content = readfile.read()

        os.remove("usblist.txt")

        if TARGET_SERIAL not in content:
            os.system("shutdown -l")  # Log off the user
            break  # Optional: break loop after logoff command
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)  # Retry after short delay if something goes wrong
