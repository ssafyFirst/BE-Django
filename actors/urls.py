from django.urls import path
from . import views

urlpatterns = [
    path('', views.actor_list),
    path('<int:actor_pk>/', views.movie_actor)
]