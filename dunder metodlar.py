# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 14:54:44 2023

@author: Quvonchbek
"""
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
def __repr__(self):# obyekt haqida tushunarli ma'lumot olamiz
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}" # natija Avto: Qora GM Malibu
def __eq__(self,boshqa_avto):
    """Tenglik"""
    return self.narh == boshqa_avto.narh

def __lt__(self,boshqa_avto):
    """Kichik"""
    return self.narh<boshqa_avto.narh

def __le__(self,boshqa_avto):
    """Kichik yoki teng"""
    return self.narh<=boshqa_avto.narh

avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1) # obyekt haqida ma'lumot olamiz
# Taqqoslashning metodlari:
# x.__lt__(self,y)  x<y
# x.__le__(self,y) x<=y
# x.__gt__(self,y) x>y
# x.__ge__(self,y) x>=y
# x.__eq__(self,y) x==y
# x.__ne__(self,y) x!=y
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto1>avto2 # TypeError: '>' not supported between instances of 'Avto' and 'Avto'
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
print(avto1>avto2) #natija: False
avto3 = Avto("Honda","Accord","Oq",2017,40000)
print(avto1==avto3)
# obyektni uzunligi
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __getitem__(self,index):# obyektga murajat qilish
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
            if isinstance(value,Avto):
               self.avtolar[index]=value
        
    def add_avto(self,avto):
        for avto in [avto1, avto2, avto3]: 
            if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
                self.avtolar.append(avto)
            else:
            
                print("Avto obyketini kiriting")  
        
    def __len__(self):
        return len(self.avtolar)
    def __call__(self,*qiymat):
          if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
            else:
                return [avto for avto in self.avtolar]
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
# Avto obyektlarini yaratamiz
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)
avto7 = Avto("BMW", 'X7','Qora',2015,75000)
# Yuqoridagi obyektlarni salon1 ga qo'shamiz
# salon1.add_avto(avto)
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")
salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)
# >>> print(len(salon1))
3 # Salonimizda 3 ta moshina bor
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
salon1[0]=avto4
print(salon1[0])









