import wakeonlan
from dotenv import load_dotenv
import os

# environment variables
load_dotenv()

# fetch mac
mac = os.getenv("MAC_ADDRESS")

if mac:
  wakeonlan.send_magic_packet(mac)
  print(f"Magic vibrations sent to {mac} to wake that mutha fucka up!")
else:
  print("MAC_ADDRESS is a mystery to the .env")