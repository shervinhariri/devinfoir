from django.shortcuts import render
import requests
#weather
from .models import City
from .forms import CityForm
#news
from bs4 import BeautifulSoup
import urllib.request
import time
# Create your views here.

def home(request):
    url_source = urllib.request.urlopen('https://news.yahoo.com/').read()
    soup = BeautifulSoup(url_source, 'html.parser')
    a_list = soup.find_all('a', 'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)')
	
    city_weather = []
	
    for a in a_list:
        if a.text not in city_weather:
            city_weather.append(a.text)
	
    context = {'city_weather': city_weather}
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

