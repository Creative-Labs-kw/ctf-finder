import requests
from bs4 import BeautifulSoup
import re
import pyperclip

def print_flag_line(line):
    formatted_line = f"\033[1;33;1m{line.strip()}\033[0m"
    print("-------------")
    print(formatted_line)
    print("-------------")
    pyperclip.copy(line.strip())
    print("Flag part copied to clipboard.")

# Define the pattern as a variable
pattern = r'flag'  # Example pattern for flags in the format picoCTF{...}

def fetch_and_filter(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        content = response.text
        lines = content.split('\n')  # Split the content into lines

        found_flag_parts = []  # List to collect found flag parts

        print(f"Lines containing the flag on the webpage {url}:")
        for line in lines:
            if re.search(pattern, line):
                found_flag_parts.append(line.strip())
                print_flag_line(line)
    
        # Parse the HTML content for links to other web pages
        soup = BeautifulSoup(content, 'html.parser')
        links = soup.find_all('a', href=True)

        for link in links:
            link_url = link['href']
            if link_url.startswith(('http://', 'https://')):  # Filter out relative links
                found_flag_parts.extend(fetch_and_filter(link_url))  # Recursively fetch and filter linked pages

        return found_flag_parts  # Return the found flag parts
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching the webpage {url}: {e}")
        return []  # Return an empty list in case of an error
    except Exception as e:
        print(f"An error occurred: {e}")
        return []  # Return an empty list in case of an error

if __name__ == "__main__":
    url = input("Enter the URL: ")
    found_parts = fetch_and_filter(url)
    
    if found_parts:
        print("Found flag parts:")
        for part in found_parts:
            print_flag_line(part)
    else:
        print("No flag parts found.")
