# get_flag_from_hash.py
import requests
import re

def print_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")

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
                return matches[0]
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
