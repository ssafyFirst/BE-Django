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
                actor_ids = []
                # movies['id'] 로 person/popular 에 요청 보내기 
                request_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
                actors = requests.get(request_url).json()
                for actor in actors['cast']:
                    # 그 영화에 출현한 actor ids 담기
                    actor_ids.append(actor['id'])
                    if len(actor_ids) > 3:
                        break

                if len(actor_ids) < 3:
                    actor_ids.extend([0, 0, 0])
                        
                fields = {
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'backdrop_path' : movie['backdrop_path'],
                    'vote_average' : movie['vote_average'],
                    'vote_count' : movie['vote_count'],
                    'original_language' : movie['original_language'],
                    'actor1' : actor_ids[0],
                    'actor2' : actor_ids[1],
                    'actor3' : actor_ids[2],
                }

                data = {
                    "pk": movie['id'],
                    "model": "movies.movie",
                    "fields": fields
                }            
                total_data.append(data)

    with open("./movies/fixtures/movie.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=2, ensure_ascii=False)

get_movie_datas()


# person/popular
def get_actor_date() :
    total_data = []

    # 1페이지부터 1000페이지까지 있음
    for i in tqdm(range(1, 501)):
        request_url = f"https://api.themoviedb.org/3/person/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        actors = requests.get(request_url).json()
        

        for actor in actors['results']:
            movie_id = []
            for movie in actor['known_for']:
                movie_id.append(movie['id'])
                if len(movie_id) > 3:
                            break

            if len(movie_id) < 3:
                movie_id.extend([0, 0, 0])

            if actor['known_for_department'] == 'Acting':                          
                fields = {
                    'name':actor['name'],
                    'profile_path' : actor['profile_path'],
                    'gender' : actor['gender'],
                    'movie1' : movie_id[0],
                    'movie2' : movie_id[1],
                    'movie3' : movie_id[2],

                }

                data = {
                    "pk": actor['id'],
                    "model": "actors.actor",
                    "fields": fields
                }

                total_data.append(data)

    with open("./actors/fixtures/actor_data.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent=2, ensure_ascii=False)

# get_actor_date()