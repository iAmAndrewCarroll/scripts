import subprocess
import time
import wakeonlan
from dotenv import load_dotenv
import os

# WoL
def wake():
  load_dotenv() # env variables
  mac = os.getenv("MAC_ADDRESS") # fetch mac address
  if mac: 
    wakeonlan.send_magic_packet(mac)
    print(f"Magic vibrations sent to CHONK to wake that mutha fucka up!")
  else:
    print("Return of the MAC...not found in env.")

# Check if Linux is up
def linux_up(ip_address):
  response = subprocess.run(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE)
  return response.returncode == 0

# Remote Desktop
def open_rdp():
  script = '''
  tell application "Microsoft Remote Desktop"
    activate
    delay 2
    connect to desktop named "CHONK"
  end tell
  '''
  subprocess.run(["osascript", "-e", script])

# step 1
wake()

# Step 2 - is CHONK ready?
chonk_ip = os.getenv("CHONK_IP")
while not linux_up(chonk_ip):
  print("Waiting for the alarm to go off...")
  time.sleep(10)

# Step 3 - Open RDP
open_rdp()