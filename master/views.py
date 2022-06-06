from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

import master
from .permissions import IsAuthor

from . import serializers
from master.models import Category, Master, Likes, Comment, Favorite


class StandartPaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000



class MasterViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Master.objects.all()
    serializer_class = serializers.MasterSerializer
    pagination_class = StandartPaginationClass
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('name',)
     #1 способ
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return serializers.MasterListSerializer
    #     else:
    #         return serializers.MasterSerializer
    #
    # def get_permissions(self): #2 способ
    #     if self.action in ['list', 'retrieve']:
    #         return [permissions.IsAuthenticated,]
    #     else:
    #         return [permissions.IsAuthenticated(),]

    @action(['GET'], detail=True)
    def comments(self, request, pk):
        master = self.get_object()
        comments = master.comments.all()
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(['POST'], detail=True)
    def add_to_liked(self, request, pk):
        master = self.get_object()
        if request.user.liked.filter(master=master).exists():
            return Response('Вы уже лайкали этот пост!', status=status.HTTP_400_BAD_REQUEST)
        Likes.objects.create(master=master, user=request.user)
        return Response('Вы поставили лайк', status=status.HTTP_201_CREATED)

    @action(['POST'], detail=True)
    def remove_from_liked(self, request, pk):
        master = self.get_object()
        if not request.user.liked.filter(master=master).exists():
            return Response('Вы не лайкали пост', status=status.HTTP_400_BAD_REQUEST)
        request.user.liked.filter(master=master).delete()
        return Response('Ваш лайк удален', status=status.HTTP_204_NO_CONTENT)


    @action(['POST'], detail=True)
    def add_to_favorites(self, request, pk):
        master = self.get_object()
        if request.user.favorites.filter(master=master).exists():
            return Response('u have already added this master to favorites', status=status.HTTP_400_BAD_REQUEST)
        Favorite.objects.create(master=master, user=request.user)
        return Response('You added it to favorites', status=status.HTTP_201_CREATED)

    @action(['POST'], detail=True)
    def remove_from_favorites(self, request, pk):
        master = self.get_object()
        if not request.user.favorites.filter(master=master).exists():
            return Response('u haven\'t added it to favorites', status=status.HTTP_400_BAD_REQUEST)
        request.user.favorites.filter(master=master, ).delete()
        return Response('The master is removed from favorites', status=status.HTTP_204_NO_CONTENT)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


    class Meta:
        model = Comment
        exclude = 'comments_detail'


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class UserAppointmentList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        user = request.user
        master = user.favorites.all()
        serializer = serializers.MasterFavoritSerializer(master, many=True).data
        return Response(serializer)