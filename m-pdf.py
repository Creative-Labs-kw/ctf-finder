import tkinter as tk
from tkinter import filedialog
import pdfplumber
import re
import pyperclip

def search_and_copy_picoCTF(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        # Define a regular expression pattern for picoCTF flags
        pattern = r'picoCTF{[^}]*}'

        found_flags = []

        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            matches = re.findall(pattern, text)

            if matches:
                found_flags.extend(matches)

        if found_flags:
            print("picoCTF Flags found:")
            for flag in found_flags:
                formatted_flag = f"Flag: {flag}"
                print(formatted_flag)
                pyperclip.copy(formatted_flag)
            print("Flags copied to clipboard")
        else:
            print("No picoCTF flags found in the PDF.")

def choose_and_process_pdf():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    pdf_file = filedialog.askopenfilename(title="Select a PDF file")

    if pdf_file:
        search_and_copy_picoCTF(pdf_file)

if __name__ == "__main__":
    choose_and_process_pdf()
