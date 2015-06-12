from rest_framework import serializers
from commerce.models import Structure
from property import PropertySerializer


class StructureSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = Structure
        fields = ('name', 'properties')