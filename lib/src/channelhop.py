import network
import time

def channel_hopping(wlan, duration=10):
    channels = list(range(1, 14))  # Channels 1 to 13
    start_time = time.time()
    while time.time() - start_time < duration:
        for channel in channels:
            wlan.config(channel=channel)
            print(f"Switched to channel {channel}")
            time.sleep(1)  # Stay on each channel for 1 second

