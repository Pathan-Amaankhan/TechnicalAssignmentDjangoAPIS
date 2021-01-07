from django.db import models


# Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length=30, null=False)
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100, default="", null=False)
    first_name = models.CharField(max_length=30, default="", null=False)
    last_name = models.CharField(max_length=30, default="", null=False)


class User(models.Model):
    user_id = models.IntegerField(null=False)
    favourite = models.CharField(default="", max_length=255)
