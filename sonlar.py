# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:58:50 2023

@author: DELL
"""
# integers-butun sonlar ustida + - * / kabi arifmetik amallarni bajarish mumkin
a = 68
b = 22
c = a + b
print(c)
# 90
tomon = 20
yuza = tomon**2
print(yuza)
#400
# floats-o'nlk sonlar (,) emas (.) qo'yiladi
pi = 3.14
r = 10
print("Aylana uzinligi",pi*2*r, "ga teng")
#Aylana uzinligi 62.800000000000004 ga teng
# butun sondan o'nlif songa o'tish uchun (/) amalini bajaramiz
a = 60
b = 120
c = b/a
print(c)
# 2.0
x,y,z = 3,8,6
# yuqorida x = 3 y = 8 z = 6 ga qiymatni yuklaydi
# str() int yoki floatdagi sonlarni man]tnga,int() matn yoki float butun songa,float() matn yoki int ko'rinishidagi qiymatni o'nlik songa o'zgartiradi
ism = "Quvonchbek"
yosh = 15
malumot = ism + ' ' + str(yosh) + " yoshda"
print(malumot)
#Quvonchbek 15 yoshda
# turini tekshirish 
ism ="Quvonchbek"
yosh = 15
print(type(ism))
print(type(yosh))
#<class 'str'> ism ning turi
#<class 'int'> yosh ning turi 