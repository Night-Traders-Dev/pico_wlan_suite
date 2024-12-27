import network

def wifi_scan():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan()  # Scan for networks
    print("Available Networks:")
    for ssid, bssid, channel, RSSI, authmode, hidden in networks:
        print(f"SSID: {ssid.decode('utf-8')}, RSSI: {RSSI}, Channel: {channel}, AuthMode: {authmode}")
    return networks
