from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/india/coronavirus-live-updates-india-will-play-a-leading-role-in-global-revival-pm-modi-says/liveblog/76843875.cms")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all("div",{"class":"_1KydD"})

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times

ht_r = requests.get("https://www.hindustantimes.com/topic/coronavirus")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})