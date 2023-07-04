# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 07:22:52 2023

@author: Quvonchbek
"""
# *args usuli
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)
print(summa(4,5,6,7)) #22
print(summa(1,2,3,4,5)) # 15

# majburiy argument:
def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)
print(summa(1,2,3,4)) # 10
print(summa(1))
# TypeError: summa() missing 1 required positional argument: 'y'

# kwargs usuli:
def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto1)
# {'rang': 'qora', 'yil': 2018, 'kompaniya': 'GM', 'model': 'malibu'}