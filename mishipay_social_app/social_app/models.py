from django.db import models

class User(models.Model):
    username = models.CharField(primary_key=True, unique=True, max_length=200)
    password = models.CharField(max_length=200)