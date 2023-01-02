from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=20)