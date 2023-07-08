from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser

class CustomAdmin(UserAdmin):
    add_form=CustomUserCreationForm,
    model=CustomUser,
    

# Register your models here.
admin.site.register(CustomUser,CustomAdmin)