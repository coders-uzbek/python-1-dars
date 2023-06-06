# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:11:47 2023

@author: QUVONCHBEK
"""
sonlar = [1,2,3,4,5] 
print("1-son: ", sonlar[0])
print("2-son: ",sonlar[1])
#1-son:  1
#2-son:  2
sonlar = [1200,1300,1500]
print(sonlar[0]+sonlar[2])
#2700
print(sonlar[-1])
#1500
# append() metodi yordamida elementlarni qo'shamiz:
oziq = ['non','olma','anjir','tarvuz']
oziq.append('shaftoli')
print(oziq)
#['non', 'olma', 'anjir', 'tarvuz', 'shaftoli']
oziq.insert(0, 'qovun')
print(oziq)
# ['qovun', 'non', 'olma', 'anjir', 'tarvuz', 'shaftoli']
del oziq[0]
print(oziq)
#['non', 'olma', 'anjir', 'tarvuz', 'shaftoli']
oziq.remove('tarvuz')
print(oziq)
# ['non', 'olma', 'anjir', 'shaftoli']
mahsulot = oziq.pop(1)
print(mahsulot)
 
