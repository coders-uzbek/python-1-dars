# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:06:05 2023

@author: QUVONCHBEK
"""
meva = ['olma','anjir','olcha','shaftoli','banan']
meva.sort()
print(meva)
#['anjir', 'banan', 'olcha', 'olma', 'shaftoli'] alifbo tartibida
meva = ['Olma','olcha','anjir','banan']
meva.sort()
print(meva)
# ['Olma', 'anjir', 'banan', 'olcha'] 1-katta harflar
meva.sort(reverse=True)
print(meva)
# ['olcha', 'banan', 'anjir', 'Olma'] teskarisi
sonlar = [12,34,76,3]
sonlar.sort()
print(sonlar)
print(sorted(sonlar, reverse=True))
# [3, 12, 34, 76]
#[76, 34, 12, 3]
sonlar.reverse()
print(meva)
# ['olcha', 'banan', 'anjir', 'Olma'] teskarisi
print("Mevalar soni:", len(meva))
# Mevalar soni: 4
son = list(range(0,10))
print(son)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 10 kirmaydi
j_sonlar = list(range(0,20,2))
print(j_sonlar)
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] juft sonlar
kichik = min(j_sonlar)
katta = max(j_sonlar)
y_sonlar = sum(j_sonlar)
print(kichik,katta,y_sonlar)
# 0 18 90   0 eng kichik 18 eng katta 90 yig'indi
car = ['audi','bnw','mers','volvo','tesla']
my_car = car[0:3]
print(my_car)
# ['audi', 'bnw', 'mers']
sonlar = [1,2,3,4,5,6]
sonlar2 = sonlar[:]
sonlar2.append(7)
sonlar2.append(8)
print("Bu sonlar ro'yhati:",sonlar)
print("Bu sonlar ro'yhati:",sonlar2)
# Bu sonlar ro'yhati: [1, 2, 3, 4, 5, 6]
# Bu sonlar ro'yhati: [1, 2, 3, 4, 5, 6, 7, 8]


 
