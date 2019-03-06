from django.shortcuts import render
from .models import Hero
from rest_framework import generics
from .serializers import HeroSerializer
# Create your views here.


class HeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    class Meta:
        model = Hero
        fields = ('id', 'name')