from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets,permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer