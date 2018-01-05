import json
import os
import pathlib
import tmdbsimple as tmdb
from dotenv import load_dotenv, find_dotenv
import time

load_dotenv(find_dotenv())
tmdb.API_KEY = os.environ.get('TMDB_KEY')

# import ipdb; ipdb.set_trace()

discover = tmdb.Discover()
popular_movies = discover.movie(sort_by='popularity.desc')

movies_path = pathlib.Path('./data/movies')
movies_path.mkdir(parents=True, exist_ok=True)

(movies_path / 'GET.json').write_text(json.dumps(popular_movies))


genres = tmdb.Genres()
all_genres = genres.movie_list()

genres_path = pathlib.Path('./data/genres')

genres_path.mkdir(parents=True, exist_ok=True)

(genres_path / 'GET.json').write_text(json.dumps(all_genres))


for result in popular_movies['results']:
    if (result['id']):
        movie = tmdb.Movies(result['id'])
        print(movie.id)
        info = movie.info()
        images = movie.images()
        reviews = movie.reviews()
        detail_path = pathlib.Path('./data/movies/{}'.format(movie.id))
        detail_path.mkdir(parents=True, exist_ok=True)

        details = {
            'info': info,
            'images': images['posters'],
            'reviews': reviews['results'],
        }

        (detail_path / 'GET.json').write_text(json.dumps(details))

    time.sleep(1)  # second
