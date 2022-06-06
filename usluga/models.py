from django.db import models
from rest_auth import serializers
from rest_framework import permissions

from account.serializers import User


class Nashi_Uslugi(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()



    def __str__(self):
        return self.title

