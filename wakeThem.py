import wakeonlan

mac = 'your mac here'

wakeonlan.send_magic_packet(mac)

print(f"Magic vibrations sent to {mac} to wake that mutha fucka up!")