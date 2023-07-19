from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomAdmin(UserAdmin):
    model=CustomUser,
    

# Register your models here.
admin.site.register(CustomUser,CustomAdmin)


#token stuff  

from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

for user in CustomUser.objects.all():
    Token.objects.get_or_create(user=user)

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)