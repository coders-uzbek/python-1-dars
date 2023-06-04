# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:47:59 2023

@author: DELL
"""
# string ya'ni matn ustida amallar bajarish mumkin:
ism = 'Quvonchbek'
print("Mening ismim " + ism)
ism = 'Quvonchbek'
familiya = 'Sherboboyev'
print(ism + familiya)
# natija QuvonchbekSherboboyev.Bo'shliq qoldirish uchun ...+ ' ' +... qo'yiladi:
ism = 'Quvonchbek'
familiya = 'Sherboboyev'
print(ism + ' ' + familiya)
# f stringdan 2 va undan ortiq matnlarni birlashtirish uchun qo'llaniladi:
ism = 'Quvonchbek'
familiya = 'Sherboboyev'
ism_sharif = f"{ism} {familiya}"   
print(ism_sharif)
print(f"Mening ismim {ism}")
# matnga bo'shliq qo'shish uchun \t foydalanamiz:
print("Salom \thamaga")
# matnni yangi qatordan boshlash uchun \n foydalanamiz:
print("Salom! \nHammaga")
# upper() metodi matndagi barcha harfni kattalshtiradi:
# QUVONCHBEK SHERBOBOYEV
print(ism_sharif.upper())
# lower() aksinchi hamma harflrni kichiklashtiradi:
print(ism_sharif.lower())
#quvonchbek sherboboyev
# title() metodi har bir so'zning 1-harfini kattalashtiradi:
print(ism_sharif.title())
#Quvonchbek Sherboboyev
# capitalize() 1-so'zning 1-harfini katta qilib yozadi:
print(ism_sharif.capitalize())
#Quvonchbek sherboboyev
# strip() matn bosidagi va oxiridagi bo'shliqni olib tashlaydi
# rstrip() matn oxiridagi lstrip() esa matn boshidagi bo'shliqni olib tashlaydi 
# input funksyasi bilan foydalanuvchi bilan muloqot qilamiz