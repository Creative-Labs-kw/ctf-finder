import paramiko

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
                print(stdout.read().decode('utf-8'))
            elif command == "ls":
                print(stdout.read().decode('utf-8'))
            else:
                print("Invalid command. Use 'cat <filename>' or 'ls'.")

        # Close the SSH connection
        ssh.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    hostname = input("Enter the SSH hostname: ")
    port = int(input("Enter the SSH port: "))
    username = input("Enter the SSH username: ")
    password = input("Enter the SSH password: ")

    ssh_interact(hostname, port, username, password)
