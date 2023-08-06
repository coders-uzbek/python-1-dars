# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 07:13:02 2023

@author: Quvonchbek
"""

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
inson = Shaxs("Hasan","Alimov","FB001122",1995)
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
# Voris klass yaratish:
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012") 
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
    print(f"{talaba.get_bosqich()}-bosqich talabasi")

print(talaba.get_info())
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil 
talaba_manzil = Manzil(12,'Olmazor',"Urgut","Samarqand")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
print(talaba.manzil.get_manzil())
print(talaba.manzil.tuman)











