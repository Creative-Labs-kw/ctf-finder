import re
import tkinter as tk
from tkinter import filedialog

def print_highlighted_flags(flags):
    if flags:
        print("CTF Flags found in the SVG content:")
        for flag, line_number in flags:
            print(f"-------------")
            print(f"Line Number: {line_number}")
            print(f"Flag: {flag}")
            print(f"-------------")
    else:
        print("No CTF flags found in the SVG data.")

def choose_and_process_svg():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open a file dialog to select an SVG file
    file_path = filedialog.askopenfilename(title="Select an SVG file")

    if file_path:
        # Read the contents of the SVG file
        with open(file_path, 'r') as file:
            svg_content = file.read()

        # Define the regular expression pattern to match text within curly braces {}
        pattern = r'{[^}]*}'

        # Find all matches in the SVG content along with their line numbers
        matches = [(match.group(0), svg_content.count('\n', 0, match.start()) + 1) for match in re.finditer(pattern, svg_content)]

        # Print and highlight the matches
        highlighted_flags = []
        for flag, line_number in matches:
            highlighted_flag = flag.replace('{', '\033[1;32;40m{\033[0m').replace('}', '\033[1;32;40m}\033[0m')
            highlighted_flags.append((highlighted_flag, line_number))
        
        print_highlighted_flags(highlighted_flags)

if __name__ == "__main__":
    choose_and_process_svg()
