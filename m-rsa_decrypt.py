import math
import pyperclip


def base256(M):
    base = 256
    message256 = []
    sisa = M
    k = 0
    z = float(M)
    p = math.floor(math.log(z) / math.log(256))
    r = int(p)
    for j in range(r + 1):
        k = sisa % base
        sisa = sisa // base
        message256.append(k)
    return message256

def encode256(ascii):
    ascii256 = ""
    for i in range(len(ascii)):
        g = int(ascii[i])
        ascii256 += chr(g)
    return ascii256

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")

def main():
    N = int(input("Enter N: "))
    e = int(input("Enter e: "))
    c = int(input("Enter c: "))
    phiN = int(input("Enter phi: "))

    d = pow(e, -1, phiN)
    m = pow(c, d, N)

    print("d =", d)
    print("m =", m)
    print("m in base 256 =", base256(m))
    
    ascii_representation = base256(m)
    ascii_text = encode256(ascii_representation)

    flag = ""
    for char in ascii_text:
        flag = char + flag

    print_flag(flag)
    pyperclip.copy(flag)
    print("Flag copied to clipboard!")

if __name__ == "__main__":
    main()
