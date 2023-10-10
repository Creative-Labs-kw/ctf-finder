# not wokring yet

def rsa_decrypt(ciphertext, modulus, private_exponent):
    # Decrypt the ciphertext
    plaintext = pow(ciphertext, private_exponent, modulus)
    return plaintext

if __name__ == "__main__":
    # Input the modulus, public exponent, ciphertext, and private exponent
    N = int(input("Enter the modulus (N): "))
    e = int(input("Enter the public exponent (e): "))
    c = int(input("Enter the ciphertext (c): "))
    d = int(input("Enter the private exponent (d): "))

    decrypted_message = rsa_decrypt(c, N, d)
    print("Decrypted message:")
    print(decrypted_message)
