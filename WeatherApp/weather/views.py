from django.shortcuts import render
import requests
from .models import City

def index(request):
    appid = '2285b80bd8326f7eb1515841ab76f240'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    cities = City.objects.all()

    all_citys = []

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_citys.append(city_info)

    context = {"all_info": city_info}

    return render(request, 'weather/index.html', context)
