from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('continentsAll/', views.ContinentListALL.as_view()),
    
    path('continents/<str:continent_name>',
         views.ContinentList.as_view({'get': 'list'})),

    path('contitnets/<str:continent_name>/<str:country_name>',
         views.ContinentList.as_view({'get': 'retrieve'})),
    
    path('contitnets/<str:continent_name>/<str:country_name>/<str:city_name>/',
         views.ContinentList.as_view({'get': 'retrieve'})),

    path('countries/', views.CountryList.as_view()),
    path('cities/', views.CityList.as_view()),
    path('weather/', views.DateWeatherList.as_view()),
]
