def analyze_traffic(packets):
    """Analyze captured packets for patterns."""
    traffic_summary = {"devices": set(), "total_bytes": 0}
    for packet in packets:
        traffic_summary["devices"].add(packet.get("src_mac"))
        traffic_summary["total_bytes"] += len(packet)
    print(f"Devices: {len(traffic_summary['devices'])}, Total Data: {traffic_summary['total_bytes']} bytes")
    return traffic_summary
