import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        print(response.json())
        return response.json()['ip']
    else:
        return None
    
get_public_ip()