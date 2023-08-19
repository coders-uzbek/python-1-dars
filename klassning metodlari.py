# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 13:16:01 2023

@author: Quvonchbek
"""
class Avto:
    """Avtomobil klassi"""
    num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        Avto.num_avto += 1
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
print(avto1.num_avto)  # natija 2
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
print(Avto.num_avto) # natija 3 
# Chunki avto classning ichida 3 ta obyekt yaratdik
# Klassning xususiyatini inkaosulatsya qilish:
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        Avto.__num_avto += 1
    
    @classmethod # bu ham bir funksya
    def get_num_avto(cls):
        return cls.__num_avto
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
print(Avto.get_num_avto()) # natija 3 

        