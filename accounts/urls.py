from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'accounts'

urlpatterns = [
    path('signup2/<username>/', csrf_exempt(views.signup2)),
    path('profile/<username>/', views.profile),
]