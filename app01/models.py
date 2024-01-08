from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customed_User(models.Model):
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=20)

class Media(models.Model):
    file = models.FileField(upload_to="uploadimg/")