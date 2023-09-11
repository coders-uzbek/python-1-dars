# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:14:20 2023

@author: Quvonchbek
"""
import requests
from bs4 import BeautifulSoup


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
news = soup.find_all(class_="news-title")
print(news[0].text)