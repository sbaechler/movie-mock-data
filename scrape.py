import json
import os
import pathlib
import tmdbsimple as tmdb
from dotenv import load_dotenv, find_dotenv
import time

def delete_folder(pth):
    for sub in pth.iterdir():
        if sub.is_dir():
            delete_folder(sub)
        else:
            sub.unlink()
    pth.rmdir()

load_dotenv(find_dotenv())
tmdb.API_KEY = os.environ.get('TMDB_KEY')

# import ipdb; ipdb.set_trace()

discover = tmdb.Discover()
popular_movies = discover.movie(sort_by='popularity.desc')

movies_path = pathlib.Path('./data/movies')
delete_folder(movies_path)
movies_path.mkdir(parents=True, exist_ok=True)

(movies_path / 'GET.json').write_text(json.dumps(popular_movies))


genres = tmdb.Genres()
all_genres = genres.movie_list()

genres_path = pathlib.Path('./data/genres')

genres_path.mkdir(parents=True, exist_ok=True)

(genres_path / 'GET.json').write_text(json.dumps(all_genres))

mongo_genres = {}
mongo_movies = {}
mongo_reviews = {}

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

        mongo_movies[movie.id] = info
        mongo_reviews[movie.id] = reviews
        for genre in info['genres']:
            mongo_genres.update(genre)

        (detail_path / 'GET.json').write_text(json.dumps(details))

    time.sleep(1)  # second

# Write the Mongodb dump
mongo_path = pathlib.Path('./mongo-dump')
mongo_path.mkdir(parents=True, exist_ok=True)
(mongo_path / 'movies.json').write_text(json.dumps(list(mongo_movies.values())))
(mongo_path / 'genres.json').write_text(json.dumps(all_genres))
(mongo_path / 'reviews.json').write_text(json.dumps(list(mongo_reviews.values())))
