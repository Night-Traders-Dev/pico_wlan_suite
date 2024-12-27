import sys
import traceback

sys.path.append('../lib')

import authbypass
import monitor
import replayattack
import dos
import rogueap
import eapattack
import wifimapper
import trafficanalyzer
import phishingportal
import scan


def print_banner():
    print("""
    ================================
         WiFi Penetration Suite
    ================================
    Available Commands:
      scan                  - Scan for networks
      wep_crack             - Crack WEP keys
      weak_psk_exploit      - Exploit weak PSKs
      monitor               - Enable monitor mode
      replay                - Replay captured packets
      beacon_flood          - Perform beacon flooding
      rogue_ap              - Set up a rogue access point
      stop_rogue_ap         - Stop the rogue access point
      eapol_replay          - Replay EAPOL handshakes
      reveal_hidden         - Reveal hidden SSIDs
      analyze_traffic       - Analyze traffic patterns
      phishing              - Start phishing portal
      exit                  - Exit the shell
    """)


def parse_packets(packets_str):
    """Safely parse packet input from the user."""
    try:
        return eval(packets_str, {"__builtins__": None}, {})
    except Exception:
        print("Invalid packet data format.")
        return None


def main():
    print_banner()
    rogue_ap_instance = None

    while True:
        try:
            command = input("WiFiShell> ").strip().split()
            if not command:
                continue

            cmd = command[0]
            args = command[1:]

            if cmd == "scan":
                networks = scan.wifi_scan()
                for network in networks:
                    print(f"SSID: {network['ssid']}, RSSI: {network['RSSI']}, Channel: {network['channel']}")

            elif cmd == "wep_crack":
                if len(args) < 1:
                    print("Usage: wep_crack <packets>")
                    continue
                packets = parse_packets(args[0])
                if packets:
                    authbypass.wep_crack(packets)

            elif cmd == "weak_psk_exploit":
                if len(args) < 1:
                    print("Usage: weak_psk_exploit <SSID>")
                    continue
                ssid = args[0]
                common_passwords = ["12345678", "password", "letmein"]
                authbypass.weak_psk_exploit(ssid, common_passwords)

            elif cmd == "monitor":
                wlan = monitor.enable_monitor_mode()
                print("Monitor mode enabled.")

            elif cmd == "replay":
                if len(args) < 1:
                    print("Usage: replay <packet_data>")
                    continue
                packet = bytes(args[0], "utf-8")
                replayattack.replay_packet(packet)

            elif cmd == "beacon_flood":
                if len(args) < 1:
                    print("Usage: beacon_flood <SSID>")
                    continue
                ssid = args[0]
                dos.beacon_flood(ssid)

            elif cmd == "rogue_ap":
                if len(args) < 1:
                    print("Usage: rogue_ap <SSID> [password] [channel]")
                    continue
                ssid = args[0]
                password = args[1] if len(args) > 1 else None
                channel = int(args[2]) if len(args) > 2 else 6
                rogue_ap_instance = rogueap.create_rogue_ap(ssid, password, channel)

            elif cmd == "stop_rogue_ap":
                if rogue_ap_instance:
                    rogueap.stop_rogue_ap(rogue_ap_instance)
                    rogue_ap_instance = None
                else:
                    print("No rogue AP is currently running.")

            elif cmd == "eapol_replay":
                if len(args) < 3:
                    print("Usage: eapol_replay <packet_data> <target_mac> <ap_mac>")
                    continue
                packet = bytes(args[0], "utf-8")
                target_mac = args[1]
                ap_mac = args[2]
                eapattack.eapol_replay(packet, target_mac, ap_mac)

            elif cmd == "reveal_hidden":
                if len(args) < 1:
                    print("Usage: reveal_hidden <packets>")
                    continue
                packets = parse_packets(args[0])
                if packets:
                    wifimapper.reveal_hidden_ssids(packets)

            elif cmd == "analyze_traffic":
                if len(args) < 1:
                    print("Usage: analyze_traffic <packets>")
                    continue
                packets = parse_packets(args[0])
                if packets:
                    trafficanalyzer.analyze_traffic(packets)

            elif cmd == "phishing":
                phishingportal.start_phishing_portal()

            elif cmd == "exit":
                print("Exiting WiFiShell. Goodbye!")
                break

            else:
                print(f"Unknown command: {cmd}")

        except KeyboardInterrupt:
            print("\nExiting WiFiShell. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    main()
