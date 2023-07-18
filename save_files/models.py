from django.db import models

# Create your models here.
class SaveFile(models.Model):
    campaign_data=models.TextField(null=False,blank=False)
    current_location=models.TextField(null=True)
    user=models.ForeignKey("user_accounts.CustomUser",on_delete=models.CASCADE,)
    created_on=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)