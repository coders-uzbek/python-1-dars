# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:26:58 2023

@author: Quvonchbek
"""
# items()
talaba = {
    'ism':'quvonchbek',
    'familiya':'sherboboyev',
    'yosh':15,
    'kurs':1
    }
print(talaba.items())
# dict_items([('ism', 'quvonchbek'), ('familiya', 'sherboboyev'), ('yosh', 15), ('kurs', 1)])
# for sikli yordamida
for kalit,qiymat in talaba.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat}")
# Kalit:ism
# Qiymat:quvonchbek
# Kalit:familiya
# Qiymat:sherboboyev
# Kalit:yosh
# Qiymat:15
# Kalit:kurs
# Qiymat:1
cars = {'umar':'audi',
        'temur':'BNW',
        'sarvar':'malibu'
        }
for kalit,qiymat in cars.items():
    print(f"{kalit.title()}ning moshinasi {qiymat}")
# Umarning moshinasi audi
# Temurning moshinasi BNW
# Sarvarning moshinasi malibu
mahsulotlar = {
    'olma':300,
    'anor':500,
    'uzum':800,
    'anjir':1000
    }
print(mahsulotlar.keys())
# dict_keys(['olma', 'anor', 'uzum', 'anjir'])
print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())
# Do'kondagi mahsulotlar:
# Olma
# Anor
# Uzum
# Anjir
# tartiblash
print("Do'konimizdagi mahsulotlar:")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
# Do'konimizdagi mahsulotlar:
# Anjir
# Anor
# Olma
# Uzum
# qiymat chiqarish
print(cars.values())
# dict_values(['audi', 'BNW', 'malibu'])
print(" Odamlar quyidagi moshinalardan foydalanadi:")
for car in cars.values():
    print(car)
# Odamlar quyidagi moshinalardan foydalanadi:
# audi
# BNW
# malibu

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'hikmat':'nokia ',
    'hamida':'galaxy s9',
    'temur':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
print('Quyidagi telefonlar mavjud:')
for tel in telefonlar.values():
    print(tel)
# Quyidagi telefonlar mavjud:
# iphone x
# galaxy s9
# mi 10 pro
# nokia 
# galaxy s9
# huawei p30
# iphone x
# iphone x
# iphone x galaxy s9 takrorlandi set() funksyasi
print(' quyidagi telefonlar mavjud:')
for tel in set(telefonlar.values()):
    print(tel)
# quyidagi telefonlar mavjud:
# nokia 
# galaxy s9
# mi 10 pro
# huawei p30
# iphone x

    
