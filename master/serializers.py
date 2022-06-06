from django.db.models import Avg
from rest_framework import serializers

import master
from master.models import Category, Master, Comment, Favorite


class MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Master
        fields = '__all__'

    def is_liked(self, card):
        user = self.context.get('request').user
        return user.liked.filter(master=master).exists()


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments_detail'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['rating'] = instance.ratings.aggregate(Avg('star'))
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
        representation['owner'] = str(user)
        representation['likes_count'] = instance.likes.count()
        return representation


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'master')


class MasterListSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Master
        fields = ('id', 'name', 'image', 'description', 'ot', 'do', 'comments', 'likes', )


    def is_liked(self, master):
        user = self.context.get('request').user
        return user.liked.filter(master=master).exists()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments_detail'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['rating'] = instance.ratings.aggregate(Avg('star'))
        user = self.context.get('request').user
        if user.is_authenticated:
            representation['is_liked'] = self.is_liked(instance)
        representation['owner'] = str(user)
        representation['likes_count'] = instance.likes.count()
        return representation




class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['masters'] = MasterListSerializer(instance.masters.all(), many=True).data
        return representation

class MasterFavoritSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'



    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        representation['master'] = instance.master.name
        return representation
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['master_favorite'] = MasterFavoritSerializer(instance.masters.all(), many=True).data
    #     return representation


