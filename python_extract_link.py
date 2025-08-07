import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Disable SSL certificate verification (use with caution)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt user for URL
url = input('Enter URL: ')

try:
    # Fetch the webpage
    print(f"Fetching {url}...")
    html = urllib.request.urlopen(url, context=ctx).read()
except urllib.error.URLError as e:
    print(f"Error fetching URL: {e}")
    exit()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <a> tags and print their href attributes
tags = soup('a')
if not tags:
    print("No hyperlinks found on the page.")
else:
    print("Hyperlinks found:")
    for tag in tags:
        href = tag.get('href', None)
        if href:
            print(href)