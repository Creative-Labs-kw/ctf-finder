# m-server.py
import re
import pyperclip
import socket

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")

def connect_to_server(host, port):
    try:
        print(f"Connecting to {host}:{port}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print("Connected to the server.")
            
            data = s.recv(4096).decode('utf-8')
            flag_pattern = r'picoCTF\{[^\}]+\}'

            matches = re.findall(flag_pattern, data)
            if matches:
                print("Flags found from the server:")
                for match in matches:
                    flag = match
                    print_flag(flag)
                    try:
                        pyperclip.copy(flag)
                        print(f"{flag} Copied")
                    except Exception as e:
                        print(f"Error copying the flag to the clipboard: {e}")
            else:
                print("No flag found from the server.")

    except Exception as e:
        print(f"Error occurred while connecting to the server: {e}")

if __name__ == "__main__":
    host = input("Host: ")
    port = int(input("Port: "))
    connect_to_server(host, port)
