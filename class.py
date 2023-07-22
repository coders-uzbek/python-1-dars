# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 07:24:47 2023

@author: Quvonchbek
"""
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_fullname())

talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.ism)
# Alijon
print(talaba1.familiya)
# Valiyev
talaba2 = Talaba("Olim","Olimov",1995)
talaba3 = Talaba("Husan","Akbarov",2004)
talaba4 = Talaba("Hasan","Akbarov",2004)
print(talaba2.ism)
print(talaba4.familiya)
# Olim
# Akbarov












