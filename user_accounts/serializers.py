from rest_framework import serializers,permissions
from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CustomUser
        fields=['url','username','password',]
        
    def create(self, validated_data):
        permission_classes=[permissions.AllowAny]
        user=super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user