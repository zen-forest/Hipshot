import argparse
import sys
import re


# Flow
## 1. Run script
## 2. It asks for a URL, add one. Is says, add another? Y, or ENTER to run
## 3. Hit Y, add another (ad nauseam)
## 4. Output on desktop folder 

# Nice to have
## Make sure browser runs as headless
## How can I speed up the process?
## Loading spinner, or a progress bar? 

# Check if URL is valid 

def is_valid_url(url):
    # Use a regular expression to check if the URL is valid
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return url is not None and regex.search(url)


parser = argparse.ArgumentParser()
parser.add_argument('url', help='URL to process')

args = parser.parse_args()
url = args.url
print(url)

if is_valid_url(url):
    print("Valid URL")
    url_list = [url]
else:
    print("Invalid URL")
    exit(1)