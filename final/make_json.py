import requests
import json
from os import environ
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

TMDB_API_KEY = environ.get('TMDB_API_KEY')

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in tqdm(range(1, 501)):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        

        for movie in movies['results']:
            if movie.get('poster_path', '') and movie.get('release_date', ''):
                fields = {
                    'adult' : movie['adult'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'backdrop_path' : movie['backdrop_path'],
                    'vote_average' : movie['vote_average'],
                    'vote_count' : movie['vote_count'],
                    'original_language' : movie['original_language']
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }

                total_data.append(data)

    with open("./movies/fixtures/movie_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, ensure_ascii=False)

get_movie_datas()