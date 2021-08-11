from bs4 import BeautifulSoup
import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
url = "https://www.sephora.com/brands-list"
response = requests.get(url=url, headers=headers)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Scraping brand links and save them into a list
brand_links_list = []
brands = soup.find_all('div', id=re.compile("brands-"))

for brands_by_alphabetical_order in brands:
    for brand in brands_by_alphabetical_order.find_all('li'):
        brand_links_list.append(
            'https://www.sephora.com' + brand.a.attrs['href'])

# Write all brand links to a txt file
with open('data/brand_links.txt', 'w') as file:
    for brand_link in brand_links_list:
        file.write(f'{brand_link}\n')

print('Total number of brands is', len(brand_links_list))
