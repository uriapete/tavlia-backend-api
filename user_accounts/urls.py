from django.urls import path,include
from . import views

urlpatterns = [
    path("user_from_token/",view=views.UserInfoFromToken.as_view())
]
