
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>/', views.movie_list),
    path('<int:movie_pk>/detail/', views.movie_detail),
    path('<int:movie_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    
    path('genres/', views.genres_list),
    path('recommendation/<username>/', views.recommendation),
    path('actor/<int:movie_pk>/', views.actor_movie),
    path('movies/<int:genre_pk>/', views.like_genre),

    path('search/<keyword>/', views.search_movie),
    path('sort/<keyword>/<int:page>/', views.sort_movie),
    path('sort/<keyword>/<int:page>/2/', views.sort_movie2),

]