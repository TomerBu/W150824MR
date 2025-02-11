from bs4 import BeautifulSoup
import requests

url = 'https://www.w3schools.com/html/html_entities.asp'

response = requests.get(url)

if response.status_code != 200:
    print('Failed to fetch page')
    print(response)
    exit()

html = response.text

soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup.find_all('p')
links = soup.find_all('a')

for link in links:
    # text as usual
    print(link.text.strip())
    # href attribute link['href']
    href = link.get('href')
    href = f'https://www.w3schools.com{href}'
    print(href)

input("hit enter to continue")

for paragraph in paragraphs:
    print(paragraph.text.strip())
    input("hit enter to continue")


