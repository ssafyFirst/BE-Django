
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>/', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/comments/<int:comment_pk>', views.comment_update_or_delete),
    
]