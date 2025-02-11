import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)

html = response.text
soup = BeautifulSoup(html, 'html.parser')

all_list_items = soup.select('.ipc-metadata-list li')

for movie_li in all_list_items:
    title = movie_li.select_one('.ipc-title__text').text

    all_metadata = movie_li.select('.cli-title-metadata-item')

    year = all_metadata[0].text
    duration = all_metadata[1].text
    rating = all_metadata[2].text

    image = movie_li.select_one('.ipc-image').get('src')


    print(title, year, duration, rating, image)
