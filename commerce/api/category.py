from rest_framework import serializers, viewsets
from commerce.models import Category
from structure import StructureSerializer
from commerce.views import router


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    structures = StructureSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'structures')


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


router.register(r'categories', CategoryViewSet)