import requests
import re
import pyperclip

def decrypt_rot13(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            shift = ord('a')
            decrypted_char = chr((ord(char) - shift + 13) % 26 + shift)
        elif 'A' <= char <= 'Z':
            shift = ord('A')
            decrypted_char = chr((ord(char) - shift + 13) % 26 + shift)
        else:
            decrypted_char = char
        plaintext += decrypted_char
    return plaintext

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")
    pyperclip.copy(formatted_flag)
    print("Flag copied to clipboard!")

def get_flag_from_hash(url, hash_value):
    try:
        # Send an HTTP POST request with the hash data
        data = {'hash': hash_value}
        response = requests.post(url, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Use regular expressions to extract the flag
            flag_pattern = r'CTF\s*{[^}]*}'
            matches = re.findall(flag_pattern, response.text)
            
            if matches:
                return decrypt_rot13(matches[0])  # Decrypt ROT13 before returning
            else:
                return "No flag found in the response."
        else:
            return f"Request failed with status code: {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

if __name__ == "__main__":
    url = input("Enter the URL: ")
    hash_value = input("Enter the hash value: ")

    flag = get_flag_from_hash(url, hash_value)
    print_flag(flag)
