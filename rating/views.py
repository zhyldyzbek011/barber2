
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.views import APIView

from master.permissions import IsAuthor, IsOwnerOrReadOnly
from . import serializers
from .models import Rating
from .parser import get_html, get_data, url

from .serializers import CreateRatingSerializer

def get_client_ip(request):
    """Получение IP пользоваеля"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга фильму"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ParsingView(APIView):

    def get(self, request):

        parsing = get_data(get_html(url))

        return Response(parsing)

