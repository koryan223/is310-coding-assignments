from bs4 import BeautifulSoup
#soup = BeautifulSoup(open("humanist_homepage.html"), features="html.parser")
import requests
import csv


response = requests.get("https://humanist.kdl.kcl.ac.uk/")


# links = soup.find_all('a')
# for link in links:
#     if 'volume' in link.text.lower():
#         print(link)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

links = soup.find_all('a')

# for link in links:
#     if "Archives" in link.get('href'):
#         print(link.get_text())
#         volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
#         volume_response = requests.get(volume_url)
#         volume_soup = BeautifulSoup(volume_response.text, "html.parser")
#         print(volume_soup.get_text())

# texts only in volumne not the link to it. Also the texts are not fomatted the same

with open('humanist_volumes.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Link', 'Volume Text'])
    for link in links:
        if "Archives" in link.get('href'):
            volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
            volume_response = requests.get(volume_url)
            volume_soup = BeautifulSoup(volume_response.text, "html.parser")
            writer.writerow([link.get_text(), volume_soup.get_text()])