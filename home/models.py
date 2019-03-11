from django.db import models

# Create your models here.

import requests

def price_print(url):
    html_data = requests.get(url).text
    ada_price = (html_data.split("ADAH19")[1].split("lastPrice"))[1][2:-2]

    return ada_price

#while True:
    #print(price_print('https://www.bitmex.com/app/trade/ADAH19'))



class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'