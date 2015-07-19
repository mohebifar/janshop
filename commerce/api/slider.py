from rest_framework import serializers, viewsets
from commerce.models import Slider
from commerce.views import router


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = ('image', 'title', 'description')


class SliderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Slider.objects.all().filter(show=True)
    serializer_class = SliderSerializer

router.register(r'sliders', SliderViewSet)