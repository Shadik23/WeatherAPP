from django.db import models

# Create your models here.

class Continent(models.Model):
    continent_name = models.CharField(max_length=264, unique=True)
    continent_img = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.continent

class Country(Continent):
    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="country")
    country_name = models.CharField(max_length=264, unique=True)
    flag = models.TextField(blank=True)

    def __str__(self):
        return self.name

class City(Country):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="city")
    city_name = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class DateWeather(City):
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="dateweather")
    date = models.DateField()
    weather_status = models.CharField(max_length=264)
    status_icon =  models.TextField(blank=True)
    wind_speed = models.IntegerField()
    humidity = models.IntegerField()
    temperatur = models.IntegerField()

    def __str__(self):
        return self.name
