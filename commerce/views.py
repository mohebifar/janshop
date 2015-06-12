from django.shortcuts import render_to_response
from rest_framework import routers


def get_index(request):
    return render_to_response('front/index.html')


router = routers.DefaultRouter()