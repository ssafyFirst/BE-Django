
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:page>/', views.movie_list)
]