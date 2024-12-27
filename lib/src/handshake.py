import network

def capture_handshake(ssid, duration=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(mode=network.MONITOR)

    print(f"Capturing WPA2 handshake packets for SSID: {ssid}...")
    start_time = time.time()
    while time.time() - start_time < duration:
        packet = wlan.recv(256)
        if b'\x88' in packet:  # Check for WPA2 handshake
            print("Captured WPA2 Handshake Packet:", packet)

