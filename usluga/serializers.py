from rest_framework import serializers

from usluga.models import Nashi_Uslugi


class Nashi_UslugiSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()

    class Meta:
        model = Nashi_Uslugi
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        return repr
