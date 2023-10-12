import re
import pyperclip  # To copy text to clipboard
import tkinter as tk
from tkinter import filedialog

def print_and_copy_flag(flag):
    if flag:
        formatted_flag = f"\033[1;33;1m{flag}\033[0m"
        print("-------------")
        print(formatted_flag)
        print("-------------")
        pyperclip.copy(flag)  # Copy the flag to the clipboard
        print("Flag copied to clipboard.")
    else:
        print("No CTF flag found in the received data.")

def choose_and_process_text():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog to select a text file
    file_path = filedialog.askopenfilename(title="Select a text file")

    if file_path:
        # Define the regular expression pattern to match picoCTF{...}
        pattern = r'picoCTF\{[^\}]+\}'

        # Check if the file exists
        with open(file_path, 'r') as file:
            text = file.read()

        # Find all matches in the text
        matches = re.findall(pattern, text)

        # Print and copy the matches
        for match in matches:
            print_and_copy_flag(match)

if __name__ == "__main__":
    choose_and_process_text()
