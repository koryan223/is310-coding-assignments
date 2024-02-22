import requests
from bs4 import BeautifulSoup
import csv

# Function to load URLs from the CSV file
def load_urls(file_path):
    urls = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            urls.append(row['link'])  # Updated to use the correct column name
    return urls

# Function to scrape the dialogue from a given URL
def scrape_dialogue(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Assuming the dialogue is within <p> tags; adjust as needed
        dialogue_text = ' '.join(p.get_text() for p in soup.find_all('p'))
        return dialogue_text[:1000]  # Return the first 1000 characters
    else:
        return f'Error: Response code {response.status_code}'

# Main script logic
if __name__ == "__main__":
    input_file_path = '/Users/baboo/Desktop/IS310/is310-coding-assignments/is310-coding-assignments/web_scraping_assignments/cleaned_pudding_data.csv' 
    output_file_path = 'pudding_movie_dialogue.csv'

    urls = load_urls(input_file_path)
    results = []

    for url in urls:
        print(f'Scraping {url}...')
        dialogue = scrape_dialogue(url)
        results.append({'url': url, 'dialogue_snippet': dialogue})
        print(f'Done with {url}')

    # Writing results to a CSV file
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['url', 'dialogue_snippet']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print('Finished scraping. Data saved to', output_file_path)

