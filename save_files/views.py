from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets,permissions
from rest_framework.parsers import JSONParser
from .models import SaveFile
from .serializers import SaveFileSerializer

# Create your views here.

class SaveFileViewSet(viewsets.ModelViewSet):
    queryset=SaveFile.objects.all().order_by("last_updated")
    serializer_class=SaveFileSerializer
    permission_classes=[permissions.IsAuthenticated]