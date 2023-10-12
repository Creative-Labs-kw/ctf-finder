import socket
import re
import tkinter as tk
from tkinter import filedialog

def send_file(filename, host, port):
    try:
        # Open the file for reading in binary mode
        with open(filename, "rb") as file:
            file_data = file.read()

        # Create a socket connection to the host and port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            # Send the file data over the socket
            client_socket.sendall(file_data)

        print(f"File '{filename}' sent successfully to {host}:{port}")

        # Receive data from the remote host
        received_data = receive_data_from_host(client_socket)

        # Find and print the CTF flag
        ctf_flag = find_ctf_flag(received_data)
        print_and_copy_flag(ctf_flag)

    except Exception as e:
        print(f"Error: {e}")

def receive_data_from_host(socket):
    try:
        received_data = b""
        while True:
            data_chunk = socket.recv(1024)
            if not data_chunk:
                break
            received_data += data_chunk

        return received_data

    except socket.error as e:
        if e.errno == 9:  # Check for "Bad file descriptor" error
            print("Socket closed by the remote host.")
        else:
            print(f"Socket error: {e}")

        return b""


def find_ctf_flag(data):
    try:
        # Define a pattern for CTF flags (modify as needed)
        pattern = r'picoCTF\{[^}]*\}'

        # Search for CTF flags in the received data
        matches = re.findall(pattern, data.decode('utf-8'))

        if matches:
            return matches[0]
        else:
            return None
    except Exception as e:
        print(f"Error while searching for CTF flag: {e}")
        return None

def print_and_copy_flag(flag):
    if flag:
        formatted_flag = f"\033[1;33;1m{flag}\033[0m"
        print("-------------")
        print(formatted_flag)
        print("-------------")
    else:
        print("No CTF flag found in the received data.")

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    filename = filedialog.askopenfilename(title="Select a file to send")  # Open file dialog
    if filename:
        host = input("Enter the remote host: ")
        port = int(input("Enter the remote port: "))
        send_file(filename, host, port)

if __name__ == "__main__":
    select_file()
