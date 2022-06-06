from rest_framework import  permissions
from rest_framework.viewsets import ModelViewSet
from . import serializers
from usluga.models import Nashi_Uslugi


class Nashi_UslugiViewSet(ModelViewSet):
    queryset = Nashi_Uslugi.objects.all()
    serializer_class = serializers.Nashi_UslugiSerializer


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
