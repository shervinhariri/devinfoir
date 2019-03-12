from bs4 import BeautifulSoup
import urllib.request
import schedule
import time

url_source = urllib.request.urlopen('https://news.yahoo.com/').read()
soup = BeautifulSoup(url_source, 'html.parser')

a_list = soup.find_all('a', 'Fw(b) Fz(20px) Lh(23px) LineClamp(2,46px) Fz(17px)--sm1024 Lh(19px)--sm1024 LineClamp(2,38px)--sm1024 Td(n) C(#0078ff):h C(#000)')

def job(a_list):
        news_file = open('data.txt', 'a+')
        for a in a_list:
                my_a = '%s\n'%str(a.text)
                #print(my_a)
                if my_a not in open('data.txt', 'r').readlines():
                        news_file.write('%s\n'%a.text)
        print(news_file)

while True:
    job(a_list)
    time.sleep(2)
