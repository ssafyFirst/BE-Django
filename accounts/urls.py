from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'accounts'

urlpatterns = [
    path('profile/<username>/', views.profile),
    # 회원수정 업데이트 url
    path('update/<username>/', views.update)
]