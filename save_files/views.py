import json
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,JsonResponse,HttpResponseBadRequest
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
    permission_classes=[permissions.IsAuthenticated,IsObjUser]
    
    def get_queryset(self):
        user=self.request.user
        return SaveFile.objects.filter(user=user).order_by("last_updated").reverse()
    
    def create(self, req:HttpRequest):
        reqbod=json.loads(req.body)
        data=dict(reqbod)
        data["user"]=req.user.pk
        serializerdata=SaveFileSerializer(data=data)
        if(serializerdata.is_valid()):
            new_save:SaveFile=serializerdata.save()
            serializer=self.get_serializer(SaveFile.objects.get(pk=new_save.pk))
            return Response(serializer.data)
        
    def update(self, request:HttpRequest, *args, **kwargs):
        reqbod=json.loads(request.body)
        data=dict(reqbod)
        data["user"]=request.user.pk
        item=self.get_object()
        serializerdata=SaveFileSerializer(item,data=data,partial=True)
        if(serializerdata.is_valid()):
            serializerdata.save()
            serializer=self.get_serializer(item)
            return Response(serializer.data)
        return HttpResponseRedirect(redirect_to="")
            