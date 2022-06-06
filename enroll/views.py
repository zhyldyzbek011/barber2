from django.contrib.auth import get_user_model
from drf_yasg.openapi import Response
from rest_framework import generics, permissions, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from enroll import serializers
from enroll.models import  Enroll

User = get_user_model()


class StandartPaginationClass(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class EnrollViewSet(ModelViewSet):
    pagination_class = StandartPaginationClass
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Enroll
        exclude = 'comments_detail'
        fields = '__all__'

    queryset = Enroll.objects.all()
    serializer_class = serializers.EnrollSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

