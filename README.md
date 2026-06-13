# 🔍 Basic Network Sniffer

A Python-based network packet sniffer that captures and analyzes live network traffic.

## 📌 Features

- Capture live network packets in real-time
- Extract source and destination IP addresses
- Identify protocol types (TCP, UDP, ICMP)
- Display port numbers for TCP/UDP traffic
- Show packet payload data

## 🛠️ Technologies Used

| Technology   | Purpose                 |
| ------------ | ----------------------- |
| Python 3.13+ | Programming language    |
| Scapy        | Packet capture library  |
| Npcap        | Windows packet driver   |
| VS Code      | Development environment |

## 🚀 How to Run

### Windows

1. Open VS Code as Administrator
2. Run: `python sniffer.py` or `py sniffer.py`

### macOS/Linux

```bash
sudo python3 sniffer.py

OUTPUT OF CODE

==================================================
Protocol: TCP
Source IP: 142.250.185.46
Destination IP: 192.168.1.100
Source Port: 443
Destination Port: 54321
==================================================

Project Structure

network-sniffer/
├── sniffer.py          # Main Python script
├── README.md           # Documentation
└── requirements.txt    # Dependencies
```
