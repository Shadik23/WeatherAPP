from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContinentSerializers, CountrySerializers, CitySerializers, DateWeatherSerializers
from .models import Continent, Country, City, DateWeather
from django.db.models import Prefetch
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.
class ContinentListALL(APIView):
    def get(self, request, format=None):
        continents = Continent.objects.all()
        serializer = ContinentSerializers(continents, many=True)
        return Response(serializer.data)
    
class ContinentList(viewsets.ViewSet):
    def list(self, request, continent_name=None):
        queryset = Continent.objects.all()
        user = get_object_or_404(queryset, continent_name=continent_name)
        serializer = ContinentSerializers(user)
        return Response(serializer.data)
    
    def retrieve(self, request, continent_name=None, country_name=None, city_name=None):
        if country_name and city_name:
            
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch('city', queryset=Country.objects.filter(
                    country_name=country_name).prefetch_related(
                Prefetch('city', queryset=City.objects.filter(city_name=city_name)))
                )
            )
        else:
            queryset = Continent.objects.filter(continent_name=continent_name).prefetch_related(
                Prefetch("country", queryset=Country.objects.filter(
                    country_name=country_name))
            )
        
        serializer = ContinentSerializers(queryset, many=True)

        return Response(serializer.data)
    
class CountryList(APIView):
    def get(self, request, format=None):
        country = Country.objects.all()
        serializer = CountrySerializers(country, many=True)
        return Response(serializer.data)
    
class CityList(APIView):
    def get(self, request, format=None):
        city = City.objects.all()
        serializer = CitySerializers(city, many=True)
        return Response(serializer.data)
    
class DateWeatherList(APIView):
    def get(self, request, format=None):
        dateweather = DateWeather.objects.all()
        serializer = DateWeatherSerializers(dateweather, many=True)
        return Response(serializer.data)