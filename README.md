README.md
Network Packet Sniffer

A Python-based network packet sniffer developed using Scapy.

Features
Captures live network packets
Detects TCP, UDP and ICMP traffic
Displays source and destination IP addresses
Saves captured packets into PCAP format
Compatible with Wireshark for packet analysis

Tools Used

Python 3
Scapy
Kali Linux
Wireshark

Installation
pip install scapy

Run
sudo python3 sniffer.py
Output

Packets are displayed in real time and stored in a PCAP file for further analysis.

Skills Demonstrated

Packet Analysis
Network Monitoring
TCP/IP Protocols
Cybersecurity Fundamentals

wrpcap("/home/kali/capture.pcap", packets)

print("\nPackets saved successfully!")
print("Saved as /home/kali/capture.pcap")
