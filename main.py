import tkinter as tk
from tkinter import filedialog
import re
import pyperclip
import subprocess
import os

def print_flag(flag):
    # ANSI escape codes for yellow color, bold, and increased text size
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    
    # Print the flag
    print("-------------")
    print(formatted_flag)
    print("-------------")

def check_file_for_flag(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            # Use a single regular expression pattern to match both CTF and picoCTF flags
            flag_pattern = r'(CTF{[^}]+})|(picoCTF{[^}]+})'
            matches = re.findall(flag_pattern, contents)
            
            if matches:
                print("Flags found in the file:")
                for match in matches:
                    flag = match[0] or match[1]
                    print_flag(flag)                   
                    try:
                        pyperclip.copy(flag)
                        print(f"{flag} Copied")
                    except Exception as e:
                        print(f"Error copying the flag to the clipboard: {e}")
            else:
                print("No flag found in the file.")

    except Exception as e:
        print(f"Error occurred while checking the file: {e}")

def search_for_picoCTF_in_directory(directory_path):
    try:
        result = subprocess.run(['grep', '-r', 'picoCTF', directory_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding='utf-8')
        decoded_result = result.stdout
        
        if decoded_result:
            print("Flags found in files:")
            print(decoded_result)
        else:
            print("No flags found in the directory.")

    except Exception as e:
        print(f"Error occurred while searching for flags in the directory: {e}")

def choose_file_or_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    file_path = filedialog.askopenfilename()
    if file_path:
        if os.path.isdir(file_path):
            search_for_picoCTF_in_directory(file_path)
        elif file_path.endswith('.zip'):
            unzip_and_grep(file_path)
        else:
            if file_path.endswith('.bin'):
                extract_flag_from_binary(file_path)
            else:
                check_file_for_flag(file_path)
    else:
        print("No file or directory selected. Please choose a valid file or directory.")

def unzip_and_grep(zip_file_path):
    try:
        result = subprocess.run(['unzip', '-c', zip_file_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding='latin-1')
        decoded_result = result.stdout

        # Define a regular expression pattern to search for the flag
        flag_pattern = r'picoCTF\{[^\}]+\}'  # Example pattern for flags in the format picoCTF{...}

        # Use a set to store unique flags
        unique_flags = set()

        # Search for and print unique flags in the contents
        for match in re.finditer(flag_pattern, decoded_result):
            flag = match.group(0)  # Extract the matched flag
            unique_flags.add(flag)

        if unique_flags:
            print("Flags found in the ZIP file:")
            for flag in unique_flags:
                print_flag(flag)
                try:
                    pyperclip.copy(flag)  # Copy the flag to the clipboard
                    print(f"{flag} Copied")
                except Exception as e:
                    print(f"Error copying the flag to the clipboard: {e}")
        else:
            print("No flag found in the ZIP file.")

    except Exception as e:
        print(f"Error occurred while unzipping and searching for flags in the ZIP file: {e}")

def extract_flag_from_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            contents = file.read().decode('latin-1')  # Read the binary file as text

            # Define a regular expression pattern to search for the flag
            flag_pattern = r'picoCTF\{[^\}]+\}'  # Example pattern for flags in the format picoCTF{...}

            # Search for the flag pattern in the contents
            match = re.search(flag_pattern, contents)

            if match:
                flag = match.group(0)  # Extract the matched flag
                print("Flag found in the binary file:")
                print_flag(flag)
                try:
                    pyperclip.copy(flag)  # Copy the flag to the clipboard
                    print(f"{flag} Copied")
                except Exception as e:
                    print(f"Error copying the flag to the clipboard: {e}")
            else:
                print("No flag found in the binary file.")

    except Exception as e:
        print(f"Error occurred while checking the binary file: {e}")

if __name__ == "__main__":
    print("Choose a file to check for CTF flags, a ZIP file to search for 'picoCTF', or a directory to search for 'picoCTF'.")
    choose_file_or_directory()
