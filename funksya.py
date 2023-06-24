# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 08:33:30 2023
@author: Quvonchbek
"""
def salom_berilsin():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")
    
def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber('quvonchbek')
# ma'lumot:
print(salom_ber.__doc__)
# Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya 

def ism_sharif(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
ism_sharif('quvonchbek','sherboboyev')

def yoshni_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")
yoshni_hisobla('quvonchbek',2008)
yoshni_hisobla(tugilgan_yil=2008,ism='quvonchbek')

def yoshni_hisobla(tugilgan_yil, joriy_yil=2023): 
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
yoshni_hisobla(2008,2023) # yoki
yoshni_hisobla(2008)
