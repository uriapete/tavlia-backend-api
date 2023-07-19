from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CustomUser
        fields=['url','username','password',]
        
    def create(self, validated_data):
        user=super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user