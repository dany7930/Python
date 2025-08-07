import urllib.request
import json
import ssl

# IP Geolocation API (Free tier available)
IP_GEOLOCATION_API = 'http://ip-api.com/json/'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_geolocation(ip_or_url):
    # Construct the API URL
    url = IP_GEOLOCATION_API + ip_or_url

    print('Retrieving', url)
    try:
        with urllib.request.urlopen(url, context=ctx) as uh:
            data = uh.read().decode()
            print('Retrieved', len(data), 'characters', data[:50].replace('\n', ' '))

            js = json.loads(data)
            if js.get('status') == 'fail':
                print('==== Error: Invalid IP or URL ====')
                print(js.get('message', 'Unknown error'))
                return None

            return js

    except Exception as e:
        print('==== Error retrieving data ====')
        print(e)
        return None

while True:
    ip_or_url = input('Enter IP address or URL (or press Enter to quit): ').strip()
    if not ip_or_url:
        break

    geolocation_data = get_geolocation(ip_or_url)
    if geolocation_data:
        print('\nGeolocation Details:')
        print('IP:', geolocation_data.get('query'))
        print('Country:', geolocation_data.get('country'))
        print('Region:', geolocation_data.get('regionName'))
        print('City:', geolocation_data.get('city'))
        print('ZIP Code:', geolocation_data.get('zip'))
        print('Latitude:', geolocation_data.get('lat'))
        print('Longitude:', geolocation_data.get('lon'))
        print('ISP:', geolocation_data.get('isp'))
        print('Organization:', geolocation_data.get('org'))
    else:
        print('Failed to retrieve geolocation data.')