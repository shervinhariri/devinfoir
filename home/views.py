from django.shortcuts import render
import requests
#weather
from .models import City
from .forms import CityForm
# Create your views here.

def home(request):
    url = "https://samples.openweathermap.org/data/2.5/weather?q={}&appid=d65ccd0817e9d7c575c724e6cec8c671"
    city = "Las vegas"

    response = requests.get(url.format(city)).json()

    city_weather = {
        "city": city,
        "temp": response["main"]["temp"]
    }
    print(city_weather)

    context = {"city_weather": city_weather}
    return render(request, 'home/home.html', context)


def bitmex(request):
    return render(request, 'home/bitmex.html')



def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d65ccd0817e9d7c575c724e6cec8c671'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'home/weather.html', context)

