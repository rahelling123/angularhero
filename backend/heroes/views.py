from django.shortcuts import render
from rest_framework.response import Response

from .models import Hero
from rest_framework import generics
from .serializers import HeroSerializer
# Create your views here.


class HeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    class Meta:
        model = Hero
        fields = ('number', 'name')


class HeroDetail(generics.GenericAPIView):
    serializer_class = HeroSerializer

    def get(self, request, number):
        hero_detail = Hero.objects.get(number=number)
        serializer = HeroSerializer(hero_detail)
        return Response(serializer.data)

    def put(self, request, number):
        hero_detail = Hero.objects.get(number=number)
        # hero_detail.name = request.data.get("name")
        hero_detail.save()
        serializer = HeroSerializer(hero_detail)
        return Response(serializer.data)



    class Meta:
        model = Hero
        fields = ('number', 'name')