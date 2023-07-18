from rest_framework import serializers
from .models import SaveFile

class SaveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model=SaveFile
        fields=['campaign_data','current_location','user','created_on','last_updated']