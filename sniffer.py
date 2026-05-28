from scapy.all import sniff, wrpcap, IP, TCP, UDP, ICMP
import datetime

packets = []
packet_count = 0


def show_packet(packet):
    global packet_count

    packet_count += 1
    packets.append(packet)

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        now = datetime.datetime.now().strftime("%H:%M:%S")

        protocol = "OTHER"

        if packet.haslayer(TCP):
            protocol = "TCP"

        elif packet.haslayer(UDP):
            protocol = "UDP"

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        print(f"[{now}] #{packet_count} [{protocol}] {src} --> {dst}")


print("Starting Packet Sniffer...")
print("Capturing 20 packets...\n")

sniff(
    iface="eth0",
    prn=show_packet,
    count=20,
    store=False
)

wrpcap("/home/kali/capture.pcap", packets)

print("\nPackets saved successfully!")
print("Saved as /home/kali/capture.pcap")