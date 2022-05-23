from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('signup2/', views.signup2),
    path('profile/<username>/', views.profile),
]