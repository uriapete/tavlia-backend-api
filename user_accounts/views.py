import json
from django.http import HttpRequest,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
class UserInfoFromToken(APIView):
    def get(self,request:HttpRequest):
        tokenKey=json.loads(request.body)["token"]
        
        tokenUser=Token.objects.get(key=tokenKey).user.username
        print((tokenUser))
        return JsonResponse({
            "user":tokenUser
        })