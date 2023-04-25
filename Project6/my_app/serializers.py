from rest_framework import serializers
from .models import Continent, Country, City, DateWeather


class DateWeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = DateWeather
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    dateweather = DateWeatherSerializers(many=True, read_only=True)

    class Meta:
        model = City
        fields = '__all__'

class CountrySerializers(serializers.ModelSerializer):
    city = CitySerializers(many=True, read_only=True)
    class Meta:
        model = Country
        fields = '__all__'

class ContinentSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True, read_only=True)
    class Meta:
        model = Continent
        fields = '__all__'




