import network
import time

def password_test(ssid, password_list):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    for password in password_list:
        print(f"Trying password: {password}")
        wlan.connect(ssid, password)
        time.sleep(2)
        if wlan.isconnected():
            print(f"Password found: {password}")
            return password
    print("No password matched.")
    return None

def generate_passwords(length=8):
    from itertools import product
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for combo in product(chars, repeat=length):
        yield ''.join(combo)

