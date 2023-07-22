# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 05:34:44 2023

@author: Quvonchbek
"""
import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi,10))
# 62.83185307179586

product = lambda x, y : x ** y
print(product(3, 2))
# 9

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")
# 3-ning kvadrati 9 ga, kubi 27 ga teng

from math import sqrt # sqrt - kvadrat ildizni hisoblaydi

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x

print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# osonroq usuli:
kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)
# [11, 13, 15]

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
juft_sonlar = list(filter(lambda son: son%2==0,sonlar)) # juft sonlar

print(sonlar)
print(juft_sonlar)
# [7, 92, 94, 5, 62, 1, 93, 61, 90, 26]
# [92, 94, 62, 90, 26]

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar)) # startswith() bosh harfini 
print(mevalar_b)
# ['banan']

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar2)
# ['olma', 'anor', 'anjir', "o'rik", 'qovun', 'banan']

bosh_oxir = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)) # endswith() oxirgi harfini
print(bosh_oxir)
# ['anor', 'anjir']


