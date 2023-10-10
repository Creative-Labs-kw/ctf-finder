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

def main():
    ciphertext = input("Enter the ROT13-encoded message: ")
    plaintext = decrypt_rot13(ciphertext)
    print("Decrypted message:")
    print(plaintext)

if __name__ == "__main__":
    main()
#EX: cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}