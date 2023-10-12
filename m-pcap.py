# THIS WILL SHOW STREAM DATA(PICO:Packets Primer)

import tkinter as tk
from tkinter import filedialog
from scapy.all import *
import re
import pyperclip

def packet_handler(packet):
    if TCP in packet and Raw in packet:
        data = packet[Raw].load.decode("utf-8", errors="ignore")
        if data:
            print(f"TCP Stream Data: {data}")

        # Search for CTF flags (assuming they are in the format 'picoCTF{...}')
        ctf_flags = re.findall(r'picoCTF{[^}]*}', data)
        if ctf_flags:
            print("CTF Flags found:")
            for flag in ctf_flags:
                formatted_flag = f"\033[1;33;1m{flag}\033[0m"
                print(f"Flag: {formatted_flag}")
                pyperclip.copy(formatted_flag)
                print("Flag copied to clipboard")

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

