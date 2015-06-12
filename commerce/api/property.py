from rest_framework import serializers
from commerce.models import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('name',)