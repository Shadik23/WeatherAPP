from django.contrib import admin
from .models import Continent, Country, City, DateWeather

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)


@admin.register(DateWeather)
class DateWeatherAdmin(admin.ModelAdmin):
    list_display = ['city', 'date']