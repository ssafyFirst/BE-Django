from django.test import TestCase

# Create your tests here.

import requests
import json
from os import environ
from dotenv import load_dotenv
from tqdm import tqdm
from movies.models import Movie

load_dotenv()

TMDB_API_KEY = environ.get('TMDB_API_KEY')

movies = Movie.objects.values('pk').all()[:10]
print(movies)

def get_moive_actor_date() :
    total_data = []

    # 1페이지부터 1000페이지까지 있음
    for i in tqdm(range(1, 10)):
        request_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        actors = requests.get(request_url).json()
        

        for actor in actors['results']:
            acting_movie = []
            if actor.get('profile_path', '') and actor['known_for_department'] == 'Acting':
                for i in actor['known_for']:
                    acting_movie.append(i['id'])
                
                fields = {
                    'name':actor['name'],
                    'profile_path' : actor['profile_path'],
                    'gender' : actor['gender'],
                    'movies' : acting_movie,
                }

                data = {
                    "pk": actor['id'],
                    "model": "actors.actor",
                    "fields": fields
                }

                total_data.append(data)

    with open("./actors/fixtures/actor_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=2, ensure_ascii=False)