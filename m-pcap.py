# THIS WILL SHOW STREAM DATA(PICO:Packets Primer)

import tkinter as tk
from tkinter import filedialog
from scapy.all import *

def packet_handler(packet):
    if TCP in packet and Raw in packet:
        data = packet[Raw].load.decode("utf-8", errors="ignore")
        if data:
            print(f"TCP Stream Data: {data}")

def choose_and_process_pcap():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    pcap_file = filedialog.askopenfilename(title="Select a PCAP file")

    if pcap_file:
        capture = rdpcap(pcap_file)
        for packet in capture:
            packet_handler(packet)

if __name__ == "__main__":
    choose_and_process_pcap()
