# decimal_to_binary.py

def decimal_to_binary(decimal_num):
    try:
        # Convert the decimal number to binary
        binary_num = bin(decimal_num).replace("0b", "")

        return binary_num

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    decimal_value = input("Enter the decimal number (e.g., 42): ")

    try:
        decimal_value = int(decimal_value)
        binary_result = decimal_to_binary(decimal_value)
        print(f"The binary representation is: {binary_result}")
    except ValueError:
        print("Invalid decimal number.")

