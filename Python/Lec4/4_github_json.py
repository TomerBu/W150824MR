import requests

url = 'https://raw.githubusercontent.com/toedter/movies-demo/refs/heads/master/backend/src/main/resources/static/movie-data/movies-250.json'

res = requests.get(url)

# print(res.status_code)

json = res.json()
movie_list = json["movies"]

for movie in movie_list:
    title = movie["Title"]
    year = movie["Year"]
    actors = movie["Actors"]
    
    print(f"{title} | ({year} | {actors})")