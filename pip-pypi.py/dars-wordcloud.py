# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:59:12 2023

@author: Quvonchbek
"""
import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt


sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)
# pprint(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())
news = soup.find_all(class_="news-title")
matn = ""
for n in news:
    matn += n.text

stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]
wordcloud = WordCloud(
    width=1000,
    height=1000,
    background_color="white",
    stopwords=stopwords,
    min_font_size=20,
).generate(matn)

# plot the WordCloud image
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
