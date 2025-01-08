import requests
import time

# ===================================================================================
# Created By     : x_4rch4n63l_x & c0d3cr4cker
# Created On     : 10/20/2024 - 12:24AM
# Script Purpose : Rotate through proxies to make periodic requests to a URL.
# Description    : This script makes periodic HTTP requests to a specified URL using
#                  a rotating list of proxies. The status codes or any errors are
#                  printed to the console.
# Features       : 
#                  - Rotates through a list of proxies
#                  - Makes HTTP requests at regular intervals
#                  - Handles exceptions and prints error messages
# Usage Note     : 
#                  - Ensure the list of proxies is populated with valid proxy URLs.
#                  - Run the script to start making requests periodically.
# ===================================================================================

proxies = [
    'http://proxy1:port1',
    'http://proxy2:port2',
    'http://proxy3:port3',
]

def get_proxy():
    """Retrieve and rotate the proxy."""
    proxy = proxies.pop(0)
    proxies.append(proxy)
    return proxy

def make_request(url):
    """Make an HTTP request using a proxy."""
    proxy = get_proxy()
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy})
        print(f"Proxy: {proxy} - Status Code: {response.status_code}")
    except Exception as e:
        print(f"Proxy: {proxy} - Error: {e}")

def main():
    url = 'http://example.com'
    interval = 60 
    for _ in range(1440): 
        make_request(url)
        time.sleep(interval)

if __name__ == '__main__':
    main()
