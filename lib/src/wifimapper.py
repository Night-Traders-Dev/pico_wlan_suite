def reveal_hidden_ssids(packets):
    """Reveal hidden SSIDs from captured packets."""
    hidden_networks = [pkt for pkt in packets if pkt.get("ssid", None) is None]
    for network in hidden_networks:
        print(f"Revealed Hidden SSID: {network.get('bssid')}")
