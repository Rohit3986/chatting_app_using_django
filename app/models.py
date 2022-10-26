from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatGroup(models.Model):
    user=models.ManyToManyField(to=User)
    group_name=models.CharField(max_length=90)
    created_on=models.DateTimeField()