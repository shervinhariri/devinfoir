from django.shortcuts import render
import requests
# Create your views here.


def price_print(url):
    html_data = requests.get(url).text
    ada_price = (html_data.split("ADAH19")[1].split("lastPrice"))[1][2:-2]
    return ada_price

ada_price = price_print('https://www.bitmex.com/app/trade/ADAH19')
posts =[
    {'date': 1900,
    'title': ada_price}
]
def home(request):
    ada = {
        'data': posts
    }
    return render(request, 'home/home.html', ada)


def bitmex(request):
    return render(request, 'home/bitmex.html')
