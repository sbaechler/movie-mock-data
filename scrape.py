import json
import os
import tmdbsimple as tmdb
from dotenv import load_dotenv, find_dotenv
import time

load_dotenv(find_dotenv())
tmdb.API_KEY = os.environ.get('TMDB_KEY')

# import ipdb; ipdb.set_trace()

discover = tmdb.Discover()
popular_movies = discover.movie(sort_by='popularity.desc')

with open('data/movies.json', 'w') as f:
    json.dump(popular_movies, f)

genres = tmdb.Genres()
all_genres = genres.movie_list()

with open('data/genres.json', 'w') as f:
    json.dump(all_genres, f)

for result in popular_movies['results']:
    if (result['id']):
        movie = tmdb.Movies(result['id'])
        print(movie.id)
        info = movie.info()
        images = movie.images()
        reviews = movie.reviews()
        detail_path = 'data/movies/{}.json'.format(movie.id)

        details = {
            'info': info,
            'images': images['posters'],
            'reviews': reviews['results'],
        }

        with open(detail_path, 'w') as f:
           json.dump(details, f)

    time.sleep(1)  # second
