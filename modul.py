# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 06:25:01 2023

@author: Quvonchbek
"""
import avto_info_mod # avto_info_mod faylidan (modulini) chaqiramiz
avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
avto_info_mod.info_print(avto1)
# natija Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$
# modullarga qisqa nom berish
import avto_info_mod as aim # avto_info_mod ni qisqa nom aim bilan yozamiz
avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)
# natija Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$
# from  ...dan deb tarjima qilinadi
from avto_info_mod import avto_info, info_print
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)
# natija Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$
# funksyalarga qisqa nom berish
from avto_info_mod import avto_info as ainfo, info_print as iprint
avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)
# natija Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$
# barcha funksyalarni ko'chirib olish
from avto_info_mod import *
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)
# natija Qora GM MALIBU, avtomat korobka, 2020-yil, 40000$
# python modullari:
# math moduli sqrt() qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi
import math
x=400
print(math.sqrt(x))
# pow(x,y) - x ning y-darajasini qaytaradi
print(pow(5,5))
# pi -π ning qiymatini saqlovchi o'zgaruvchi
from math import pi
print(pi)
# log2(x) va log10(x) - x ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar
# random moduli
# randit(a,b) Bu funksiya a va b oraligi'da tasodifiy butun son qaytaradi.
import random as r 
son = r.randint(0,100) 
print(son)
# choice(x) x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz
