from rest_framework import serializers

from rating.models import Rating


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "master")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            master=validated_data.get('master', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating