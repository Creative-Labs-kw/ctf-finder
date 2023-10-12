# FOR ALL TYPE NOT separated CTF:
from PIL import Image
import pytesseract
import re

def extract_flags_from_image(image_path):
    try:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img)

        # Define a pattern to match CTF flags (picoCTF:{...})
        pattern = r'picoCTF{[^}]*}'

        # Find all CTF flags in the extracted text
        matches = [match.group(0) for match in re.finditer(pattern, extracted_text)]

        # Concatenate all flags into a single line
        concatenated_flags = ''.join(matches)

        if concatenated_flags:
            print("CTF Flags found in the extracted text:")
            print(f"----------------------")
            print(concatenated_flags)
            print(f"----------------------")
        else:
            print("No CTF flags found in the extracted text.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_path = input("Enter the path to the image file (JPEG, JPG, PNG, or SVG): ")
    extract_flags_from_image(image_path)
