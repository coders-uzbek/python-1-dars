# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:55:14 2023

@author: Quvonchbek
"""
import requests
import googletrans

url = "https://api.adviceslip.com/advice"
r = requests.get(url)
advice = r.json()["slip"]["advice"]
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest="uz")
print(tarjima.text)
