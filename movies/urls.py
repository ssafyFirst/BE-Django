
from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>/', views.movie_list),
    path('<int:movie_pk>/comments/<int:comment_pk>', views.comment_update_or_delete),
    
]