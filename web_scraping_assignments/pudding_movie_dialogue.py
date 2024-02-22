import requests
from bs4 import BeautifulSoup
import csv

def load_urls(file_path):
    urls = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            urls.append(row['link']) 
    return urls

def scrape_dialogue(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        dialogue_text = ' '.join(p.get_text() for p in soup.find_all('p'))
        return dialogue_text[:1000]

if __name__ == "__main__":
    input_file_path = 'cleaned_pudding_data.csv' 
    output_file_path = 'pudding_movie_dialogue.csv'

    urls = load_urls(input_file_path)
    results = []

    for url in urls:
        print(f'Scraping {url}...')
        dialogue = scrape_dialogue(url)
        results.append({'url': url, 'dialogue_snippet': dialogue})
        print(f'Done with {url}')

    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['url', 'dialogue_snippet']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

