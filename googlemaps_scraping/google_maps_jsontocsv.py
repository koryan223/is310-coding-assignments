import json
import csv

with open('places.json') as f:
    places = json.load(f)

csv_file = 'fast_food_places.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Name', 'Address', 'Latitude', 'Longitude', 'Rating'])

    for place in places:
        name = place['name']
        address = place.get('vicinity', 'N/A')
        location = place['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        rating = place.get('rating', 'N/A')

        writer.writerow([name, address, latitude, longitude, rating])
