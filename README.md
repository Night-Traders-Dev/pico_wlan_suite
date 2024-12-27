# WiFi Penetration Testing Suite

This is a **WiFi penetration testing suite** designed for the **Raspberry Pi Pico W** using **MicroPython**. The suite provides tools for ethical hacking, network analysis, and testing wireless security vulnerabilities. 

> **Disclaimer:** This tool is for **educational purposes only**. Use it only on networks you own or have explicit permission to test. Unauthorized use is illegal and punishable by law.

---

## Features

1. **Network Scanning**: Detect nearby WiFi networks and their parameters.
2. **WEP Cracking**: Analyze WEP packets to recover WEP keys.
3. **PSK Exploits**: Test common passwords against WPA/WPA2 networks.
4. **Monitor Mode**: Capture packets in raw mode for further analysis.
5. **Packet Replay**: Replay captured packets to test network resilience.
6. **Beacon Flooding**: Simulate beacon flooding with fake SSIDs.
7. **Rogue Access Point**: Create a rogue access point to test client behavior.
8. **EAPOL Replay**: Replay EAPOL handshake packets to test WPA/WPA2.
9. **Hidden SSID Reveal**: Detect and reveal hidden SSIDs.
10. **Traffic Analysis**: Analyze network traffic for patterns and vulnerabilities.
11. **Phishing Portal**: Host a phishing portal to capture credentials.

---

## Requirements

- **Hardware**: Raspberry Pi Pico W
- **Software**: MicroPython firmware
- **Environment**:
  - A PC or laptop to interact with the Pico W via USB
  - Python installed on your PC for flashing and communication

---

## Installation

1. **Set Up MicroPython**:
   - Download MicroPython firmware from the [official website](https://micropython.org/download/rp2-pico-w/).
   - Flash it onto the Pico W using a tool like `Thonny`.

2. **Clone This Repository**:
   ```bash
   git clone https://github.com/your-repo/wifi-pen-testing-suite.git
   cd wifi-pen-testing-suite
   ```
3. **Transfer Files**:

Use a tool like mpfshell or ampy to transfer the suite files to your Pico W.

```bash
mpfshell
mput -r lib
mput src/main.py
```

4. **Run the Suite**:

Ensure the main.py file is set to run on boot.

Reset your Pico W and connect via a serial terminal.




---

**Usage**

When you run the suite, you'll enter an interactive shell:

```bash
===============================
   WiFi Penetration Testing Shell
===============================
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
```
**Example Commands**

1. **Scan for Networks**:

```bash
WiFiShell> scan
```

2. **Set Up a Rogue Access Point**:

```bash
WiFiShell> rogue_ap FakeSSID FakePassword 6
```

3. **Replay EAPOL Packets**:

```bash
WiFiShell> eapol_replay "EAPOL_PACKET_DATA" "00:11:22:33:44:55" "66:77:88:99:AA:BB"
```

4. **Start a Phishing Portal**:

```bash
WiFiShell> phishing
```

5. **Exit the Shell**:

```bash
WiFiShell> exit
```



---

**Project Structure**

```bash
wifi-pen-testing-suite/
├── lib/
│   ├── authbypass.mpy       # WEP cracking and weak PSK exploits
│   ├── monitor.mpy          # Monitor mode utilities
│   ├── replayattack.mpy     # Packet replay logic
│   ├── dos.mpy              # Beacon flooding
│   ├── rogueap.mpy          # Rogue access point creation
│   ├── eapattack.mpy        # EAPOL replay attacks
│   ├── wifimapper.mpy       # Hidden SSID detection
│   ├── trafficanalyzer.mpy  # Traffic analysis
│   ├── phishingportal.mpy   # Phishing portal setup
│   └── scan.mpy             # Network scanning
└── src/
    └── main.py             # Interactive CLI shell
```

---

**Contribution**

1. **Fork this repository.**


2. **Create a new branch for your feature or fix.**


3. **Submit a pull request for review.**




---

**Disclaimer**

This tool is for educational purposes only. The authors are not responsible for any misuse or damage caused by this tool. Always ensure you have proper authorization before testing any network.


---

**License**

This project is licensed under the MIT License.
