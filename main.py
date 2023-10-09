import tkinter as tk
from tkinter import filedialog
import re
import pyperclip
import subprocess
import os

def check_file_for_flag(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            match = re.search(r'(CTF\{[^}]+\})|(\([^)]+\))|(\{[^}]+\})', contents)
            if match:
                flag = match.group(0)
                print("Flag found:", flag)
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
            check_file_for_flag(file_path)
    else:
        print("No file or directory selected. Please choose a valid file or directory.")

def unzip_and_grep(zip_file_path):
    try:
        result = subprocess.run(['unzip', '-c', zip_file_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, encoding='latin-1')
        decoded_result = result.stdout
        if 'picoCTF' in decoded_result:
            print("Flags found in the ZIP file.")
            print(decoded_result)
        else:
            print("No flags found in the ZIP file.")
    except Exception as e:
        print(f"Error occurred while unzipping and searching for flags in the ZIP file: {e}")

if __name__ == "__main__":
    print("Choose a file to check for CTF flags, a ZIP file to search for 'picoCTF', or a directory to search for 'picoCTF'.")
    choose_file_or_directory()
