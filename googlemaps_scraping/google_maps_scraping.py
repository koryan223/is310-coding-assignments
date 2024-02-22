import requests
import json
import time

api_key = ''
endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params = {
    'location': '40.10774735350193, -88.23151006005415',
    'radius': '10000',
    'type': 'restaurant',
    'keyword': 'fast food',
    'key': api_key
}

response = requests.get(endpoint, params=params)
places = response.json()
places = []
response = requests.get(endpoint, params=params).json()

if response.get('status') == 'OK':
    places.extend(response.get('results', []))
else:
    print(f"Initial API Error: {response.get('status')} - {response.get('error_message', 'No additional error message')}")

while 'next_page_token' in response:
    time.sleep(2)
    params['pagetoken'] = response['next_page_token']
    response = requests.get(endpoint, params=params).json()

    if response.get('status') == 'OK':
        places.extend(response.get('results', []))
    else:
        print(f"Pagination API Error: {response.get('status')} - {response.get('error_message', 'No additional error message')}")
        break

with open('places.json', 'w') as f:
    json.dump(places, f, indent=4)
print(f"Data written to places.json with total places: {len(places)}")