import json
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets,permissions
from .permissions import IsObjUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import SaveFile
from .serializers import SaveFileSerializer

# Create your views here.

class SaveFileViewSet(viewsets.ModelViewSet):
    
    queryset=SaveFile.objects.all().order_by("last_updated")
    serializer_class=SaveFileSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsObjUser]
    
    def create(self, req:HttpRequest):
        reqbod=json.loads(req.body)
        data=dict(reqbod)
        data["user"]=req.user.pk
        serializerdata=SaveFileSerializer(data=data)
        if(serializerdata.is_valid()):
            new_save:SaveFile=serializerdata.save()
            return HttpResponseRedirect(redirect_to=f"{new_save.pk}/")
            