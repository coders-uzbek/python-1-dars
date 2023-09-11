# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:55:41 2023

@author: Quvonchbek
"""
# pip install googletrans==3.1.0a0
from googletrans import Translator

tarjimon = Translator()

msg = 'Tarjima uchun so\'z kiriting (chiqib ketish uchun "q" deb yozing): '
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src="uz", dest="en")
        print(tarjima.text)
