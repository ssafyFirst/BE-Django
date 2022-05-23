
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>/', views.movie_list),
<<<<<<< HEAD
    path('<int:movie_pk>/detail/', views.movie_detail),
=======
    path('<int:movie_pk>/detail', views.movie_detail),
>>>>>>> 2f3f8358a8e20701d5f104e254afce10fac2d78f
    path('<int:movie_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/like', views.like_movie),
    path('<int:movie_pk>/comments/<int:comment_pk>', views.comment_update_or_delete),
    
]