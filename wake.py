import wakeonlan

mac = '90:b1:1c:68:a9:9d'

wakeonlan.send_magic_packet(mac)

print(f"Magic vibrations sent to {mac} to wake that mutha fucka up!")