import paramiko
import pyperclip

def ssh_interact(hostname, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=port, username=username, password=password)

        while True:
            command = input("Enter a command (cat/ls/exit): ").strip()
            if command == "exit":
                break

            stdin, stdout, stderr = ssh.exec_command(command)

            if command.startswith("cat"):
                flag = stdout.read().decode('utf-8')
                print_flag(flag)
            elif command == "ls":
                print(stdout.read().decode('utf-8'))
            else:
                print("Invalid command. Use 'cat <filename>' or 'ls'.")

        # Close the SSH connection
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")
    pyperclip.copy(formatted_flag)
    print("Flag copied to clipboard.")

if __name__ == "__main__":
    hostname = input("Enter the SSH hostname: ")
    port = int(input("Enter the SSH port: "))
    username = input("Enter the SSH username: ")
    password = input("Enter the SSH password: ")

    ssh_interact(hostname, port, username, password)
