from rest_framework import serializers
from commerce.models import Detail


class DetailSerializer(serializers.ModelSerializer):
    property = serializers.StringRelatedField()

    class Meta:
        model = Detail
        fields = ('id', 'value', 'property')