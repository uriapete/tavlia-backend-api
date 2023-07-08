from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomAdmin(UserAdmin):
    model=CustomUser,
    

# Register your models here.
admin.site.register(CustomUser,CustomAdmin)