# hex_to_ascii.py
import pyperclip

def hex_to_ascii(hex_str):
    try:
        # Remove '0x' prefix if present
        if hex_str.startswith("0x"):
            hex_str = hex_str[2:]

        # Convert the hexadecimal string to bytes
        bytes_data = bytes.fromhex(hex_str)

        # Convert the bytes to ASCII
        ascii_str = bytes_data.decode('ascii')

        return ascii_str

    except Exception as e:
        return str(e)

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")
    pyperclip.copy(formatted_flag)
    print("Flag copied to clipboard!")

if __name__ == "__main__":
    hex_value = input("Enter the hexadecimal value (e.g., 0x70): ")

    ascii_result = hex_to_ascii(hex_value)
    if ascii_result:
        print("The ASCII representation is:")
        print_flag(ascii_result)
    else:
        print("Invalid hexadecimal value.")
