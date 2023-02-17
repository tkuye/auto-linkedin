import argparse
import requests
from getpass import getpass
import os
import json

AUTH_REQUEST_HEADERS = {
        "X-Li-User-Agent": "LIAuthLibrary:3.2.4 \
                            com.linkedin.LinkedIn:8.8.1 \
                            iPhone:8.3",
        "User-Agent": "LinkedIn/8.8.1 CFNetwork/711.3.18 Darwin/14.0.0",
        "X-User-Language": "en",
        "X-User-Locale": "en_US",
        "Accept-Language": "en-us",
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_path', type=str, default='./data')
    parser.add_argument('--identity_name', type=str)

    args = parser.parse_args()
    res = requests.get(
            "https://www.linkedin.com/uas/authenticate",
            headers=AUTH_REQUEST_HEADERS,
            timeout=10,
        )
    cookies = res.cookies

    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    data = {
        'session_key': username,
        'session_password': password,
         "JSESSIONID": cookies["JSESSIONID"]
    }
    
    response = requests.post(
        'https://www.linkedin.com/uas/authenticate', 
        cookies=cookies,
        data=data,
        headers=AUTH_REQUEST_HEADERS,
        timeout=10,
    )
    
    if response.status_code != 200:
        print("Error: ", response.status_code, response.text)
        return
    
    print('Login successful.')
    cookies = response.cookies
    headers = response.headers
    headers['csrf-token'] = cookies['JSESSIONID']

    if not args.identity_name:
        identity = input('Give a name to this identity: ')
    else:
        identity = args.identity_name
    
    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)
    
    if not os.path.exists(os.path.join(args.save_path, identity)):
        os.makedirs(os.path.join(args.save_path, identity))

    with open(os.path.join(args.save_path, identity, 'cookies.json'), 'w', encoding='utf-8') as f:
        json.dump(cookies.get_dict(), f, indent=4)
    
    with open(os.path.join(args.save_path, identity, 'headers.json'), 'w', encoding='utf-8') as f:
        json.dump(dict(headers), f, indent=4)
    
    print('Credentials saved.')

    








if __name__ == '__main__':
    main()