from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    """This function runs for every packet captured"""
    
    # Check if packet has IP layer
    if IP in packet:
        # Get source and destination IPs
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Get protocol number and convert to name
        proto = packet[IP].proto
        if proto == 6:
            protocol = "TCP"
        elif proto == 17:
            protocol = "UDP"
        elif proto == 1:
            protocol = "ICMP"
        else:
            protocol = "Other"
        
        # Print packet info
        print(f"\n{'='*60}")
        print(f"[+] {protocol} Packet")
        print(f"    Source IP: {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        
        # Get port information for TCP/UDP
        if protocol == "TCP" and TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"    Source Port: {src_port}")
            print(f"    Destination Port: {dst_port}")
            print(f"    TCP Flags: {packet[TCP].flags}")
            
        elif protocol == "UDP" and UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"    Source Port: {src_port}")
            print(f"    Destination Port: {dst_port}")
        
        # Show payload if exists (first 50 bytes)
        if Raw in packet:
            payload = packet[Raw].load
            print(f"    Payload (first 50 bytes): {payload[:50]}")
        
        print(f"{'='*60}")

# Main program
print("="*60)
print("🔍 NETWORK SNIFFER STARTED")
print("="*60)
print("Capturing 20 packets... Press Ctrl+C to stop early\n")

# Capture 20 packets
try:
    sniff(prn=packet_callback, count=20)
    print("\n✅ Finished capturing 20 packets!")
except KeyboardInterrupt:
    print("\n\n⏹️ Sniffer stopped by user")
except PermissionError:
    print("\n❌ PERMISSION ERROR!")
    print("You need to run this as Administrator (Windows) or with sudo (Mac/Linux)")