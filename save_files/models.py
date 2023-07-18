from django.db import models

# Create your models here.
class SaveFile(models.Model):
    flags=models.IntegerField(null=True,default=0)
    current_location=models.IntegerField(null=True,default=0)
    user=models.ForeignKey("user_accounts.CustomUser",on_delete=models.CASCADE,)
    created_on=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)