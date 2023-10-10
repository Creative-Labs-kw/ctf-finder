# decimal_to_binary.py

def decimal_to_binary(decimal_num):
    try:
        # Convert the decimal number to binary
        binary_num = bin(decimal_num).replace("0b", "")

        return binary_num

    except Exception as e:
        return str(e)

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")

if __name__ == "__main__":
    decimal_value = input("Enter the decimal number (e.g., 42): ")

    try:
        decimal_value = int(decimal_value)
        binary_result = decimal_to_binary(decimal_value)
        print(f"The binary representation is: {binary_result}")
    except ValueError:
        print("Invalid decimal number.")
