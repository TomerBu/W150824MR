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


# find all images/links/paragraphs

all_images = soup.find_all('img')


for image in all_images:
    src = image.get('src') #/signup/lynxlogo.svg

    file_name = src.split('/')[-1]

    src = f'https://www.w3schools.com{src}'
    
    res = requests.get(src)

    # res.text (text), res.json (json), res.content (binary)

    binary_data = res.content
    file = open(file_name, 'wb')
    file.write(binary_data)
    file.close()



# # open a file for writing
# f = open("123.txt", 'w')

# # write to the file
# f.write("Hello files")

# # close the file
# f.close()




 