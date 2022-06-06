from django.contrib.auth import get_user_model
from django.db.models import Avg
from requests import Response
from rest_framework import serializers, status

from enroll.models import  Enroll
from rating.models import Rating

User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Rating
        fields = ('owner', 'star', 'enroll')


class EnrollSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')


    class Meta:
        model = Enroll
        fields = (
            'id', 'first_name', 'last_name', 'owner', 'category', 'phone_number', 'master', 'time', 'schedule',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        created_enroll = Enroll.objects.create(**validated_data)
        return created_enroll

