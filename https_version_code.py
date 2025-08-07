import socket
import ssl
from urllib.parse import urlparse

# Ask the user for a URL
url = input('Enter URL: ')

# Parse the URL to extract hostname and path
parsed_url = urlparse(url)
hostname = parsed_url.hostname
path = parsed_url.path if parsed_url.path else '/'

# Use port 443 for HTTPS
port = 443

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL
context = ssl.create_default_context()
mysock = context.wrap_socket(mysock, server_hostname=hostname)

# Connect to the server
mysock.connect((hostname, port))

# Send the HTTP GET request
cmd = f'GET {path} HTTP/1.0\r\nHost: {hostname}\r\n\r\n'.encode()
mysock.send(cmd)

# Receive and print the data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket
mysock.close()