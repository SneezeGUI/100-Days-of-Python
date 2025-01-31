import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

## Get Website data
response = requests.get(URL)

#make soup
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

##get all movie data
movie_data = soup.find_all(name='div', class_="article-title-description__text")
# print(movie_data)

##get movie titles and rank
movie_ranks = [movie.find(name='h3', class_='title').getText() for movie in movie_data]
print(movie_ranks)


# open a new file and write the movie data into it in reverse order
with open('best_movies.txt', 'w', encoding='utf-8') as f:
    for rank in reversed(movie_ranks):
        f.write(rank + '\n')