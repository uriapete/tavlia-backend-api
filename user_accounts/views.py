import json
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
class UserInfoFromToken(APIView):
    def get(self,request:HttpRequest):
        data={}
        if request.user.is_authenticated:
            data["user"]=request.user.username
        return JsonResponse(data)