# m-file.py
import tkinter as tk
from tkinter import filedialog
import re
import pyperclip
import subprocess
import os

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")

def check_file_for_flag(file_path):
    try:
        with open(file_path, 'rb') as file:
            contents = file.read().decode('latin-1', errors='ignore')

            matches = re.findall(r'(CTF{[^}]+})|(picoCTF{[^}]+})', contents)
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

        flag_pattern = r'picoCTF\{[^\}]+\}'
        unique_flags = set()

        for match in re.finditer(flag_pattern, decoded_result):
            flag = match.group(0)
            unique_flags.add(flag)

        if unique_flags:
            print("Flags found in the ZIP file:")
            for flag in unique_flags:
                print_flag(flag)
                try:
                    pyperclip.copy(flag)
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
            contents = file.read().decode('latin-1')

            flag_pattern = r'picoCTF\{[^\}]+\}'

            match = re.search(flag_pattern, contents)

            if match:
                flag = match.group(0)
                print("Flag found in the binary file:")
                print_flag(flag)
                try:
                    pyperclip.copy(flag)
                    print(f"{flag} Copied")
                except Exception as e:
                    print(f"Error copying the flag to the clipboard: {e}")
            else:
                print("No flag found in the binary file.")

    except Exception as e:
        print(f"Error occurred while checking the binary file: {e}")

if __name__ == "__main__":
    print("This program can check files and directories for CTF flags.")
    choose_file_or_directory()
