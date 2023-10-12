# separated PTC

from PIL import Image
import pytesseract
import re

def print_highlighted_flags(flags):
    if flags:
        print("CTF Flags found in the extracted text:")
        for flag, line_number in flags:
            print(f"-------------")
            print(f"Flag found in Line Number: {line_number}")
            print(flag)
            print(f"-------------")
    else:
        print("No CTF flags found in the extracted text.")

def extract_and_highlight_flags_from_jpg(image_path):
    try:
        # Open the JPEG image using PIL
        img = Image.open(image_path)

        # Use pytesseract to extract text from the image
        extracted_text = pytesseract.image_to_string(img)

        # Define the regular expression pattern to match text within curly braces {}
        pattern = r'{[^}]*}'

        # Find all matches in the extracted text along with their line numbers
        matches = [(match.group(0), extracted_text.count('\n', 0, match.start()) + 1) for match in re.finditer(pattern, extracted_text)]

        # Print and highlight the matches
        highlighted_flags = []
        for flag, line_number in matches:
            highlighted_flag = flag.replace('{', '\033[1;32;40m{\033[0m').replace('}', '\033[1;32;40m}\033[0m')
            highlighted_flags.append((highlighted_flag, line_number))

        print_highlighted_flags(highlighted_flags)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = input("Enter the path to the JPEG image file: ")
    extract_and_highlight_flags_from_jpg(image_path)
