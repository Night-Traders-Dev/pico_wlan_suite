import network

def create_rogue_ap(ssid, password=None, channel=6):
    """
    Create a rogue access point.

    Args:
        ssid (str): The SSID of the rogue AP.
        password (str): Optional WPA2 password for the AP.
        channel (int): The WiFi channel to use.
    """
    wlan_ap = network.WLAN(network.AP_IF)
    wlan_ap.active(True)

    if password:
        wlan_ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA2_PSK, channel=channel)
    else:
        wlan_ap.config(essid=ssid, authmode=network.AUTH_OPEN, channel=channel)

    print(f"Rogue AP created with SSID: {ssid}, Channel: {channel}, Security: {'WPA2' if password else 'Open'}")
    return wlan_ap

def stop_rogue_ap(wlan_ap):
    """
    Stop the rogue access point.

    Args:
        wlan_ap: The WLAN AP object.
    """
    wlan_ap.active(False)
    print("Rogue AP stopped.")
