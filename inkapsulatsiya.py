# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:50:55 2023

@author: Quvonchbek
"""
from uuid import uuid4 # uuid4 tasadifiy yangi id raqam qaytaradi
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km # inkapsulatsya ya'ni yashirin xususiyat
        self.__id = uuid4()# inkapsulatsya ya'ni yashirin xususiyat
    
    def get_km(self): # metodi
        return self.__km # kmni qaytaradi
    
    def get_id(self):
        return self.__id# idsini qaytaradi
avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
print(f"ID: {avto1.get_id()}")

def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:# musbat son bo'lishi kerak
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
avto1.add_km(1500)
print(avto1.get_km())
