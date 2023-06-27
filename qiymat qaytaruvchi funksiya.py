# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 06:55:41 2023

@author: Quvonchbek
"""
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism

talaba1 = toliq_ism_yasa('umar','eshmurodov')
talaba2 = toliq_ism_yasa('temur','rashidov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi: 
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()

talaba1 = toliq_ism_yasa('umar','elmurodov') #otasining_ismi kiritilmadi
talaba2 = toliq_ism_yasa('temur','abdullayev','ruziyevich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('tesla','Tesla X','Kumush','Avtomat',2016,150000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
    
def oraliq(min,max,qadam):
    sonlar = [] 
    while min<max:
        sonlar.append(min)
        min += 3
    return sonlar

print(oraliq(0,10,3))
print(oraliq(10,21,3))

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] 
while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    
    kompaniya=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break