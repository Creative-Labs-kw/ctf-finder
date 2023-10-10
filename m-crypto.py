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
    print("Decrypted message:")
    print(formatted_flag)
    print("-------------")
    pyperclip.copy(formatted_flag)
    print("Flag copied to clipboard!")

def main():
    ciphertext = input("Enter the ROT13-encoded message: ")
    plaintext = decrypt_rot13(ciphertext)
    print_flag(plaintext)

if __name__ == "__main__":
    main()
