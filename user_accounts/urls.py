from django.urls import path

from user_accounts.models import CustomUser
from . import views,include
from rest_framework import routers,serializers,viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CustomUser
        fields=['url','username']
        
class UserViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    
router=routers.DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
