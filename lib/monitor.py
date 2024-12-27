import network

def enable_monitor_mode():
    """Enable monitor mode for packet capturing."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(mode=network.MONITOR)
    print("Monitor mode enabled.")
    return wlan

def filter_packets(packets, protocol):
    """Filter packets by specific protocol."""
    filtered = [pkt for pkt in packets if pkt.get("protocol") == protocol]
    print(f"Filtered packets: {len(filtered)}")
    return filtered
