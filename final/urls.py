from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/accounts/', include('dj_rest_auth.urls')),
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/actors/', include('actors.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)