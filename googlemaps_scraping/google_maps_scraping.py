import requests
import json
import time

# Define API Key, Endpoint, and Parameters
api_key = 'AIzaSyDaTPxLlZmgYzinhTstEwLP0oEJMW8Dodk'
endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params = {
    'location': '40.10774735350193, -88.23151006005415',  # Replace with the actual latitude and longitude
    'radius': '10000',  # Search within a 5,000-meter radius
    'type': 'restaurant',
    'keyword': 'fast food',
    'key': api_key
}

response = requests.get(endpoint, params=params)
places = response.json()
places = []
response = requests.get(endpoint, params=params).json()

# Check the initial response status
if response.get('status') == 'OK':
    places.extend(response.get('results', []))
else:
    print(f"Initial API Error: {response.get('status')} - {response.get('error_message', 'No additional error message')}")

# Handle pagination with status checks
while 'next_page_token' in response:
    time.sleep(2)  # Ensure you wait for the token to become valid
    params['pagetoken'] = response['next_page_token']
    response = requests.get(endpoint, params=params).json()

    if response.get('status') == 'OK':
        places.extend(response.get('results', []))
    else:
        print(f"Pagination API Error: {response.get('status')} - {response.get('error_message', 'No additional error message')}")
        break  # Exit the loop if there's an error

# Optionally, save the aggregated results to a JSON file for further processing
with open('places.json', 'w') as f:
    json.dump(places, f, indent=4)
print(f"Data written to places.json with total places: {len(places)}")