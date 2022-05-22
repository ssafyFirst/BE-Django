from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'profile_img')

admin.site.register(User, UserAdmin)