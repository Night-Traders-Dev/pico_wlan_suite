import network

def packet_sniffer(duration=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(mode=network.MONITOR)

    print("Sniffing packets...")
    start_time = time.time()
    while time.time() - start_time < duration:
        packet = wlan.recv(256)
        if packet:
            print(packet)
