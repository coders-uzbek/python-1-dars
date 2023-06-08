# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 19:24:31 2023

@author: DELL
"""
# for bilan tanishamiz:
mehmonlar = ['Nodir','Nurbek','Asat']
for mehmon in mehmonlar:
    print(mehmon)
#Nodir
#Nurbek
#Asat
for mehmon in mehmonlar:
  print(f"Hurmatli {mehmon} sizni uyimizda kutib qolamiz")
#  Hurmatli Nodir sizni uyimizda kutib qolamiz
#  Hurmatli Nurbek sizni uyimizda kutib qolamiz
#  Hurmatli Asat sizni uyimizda kutib qolamiz
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son }ning kvadrati {son**2} ga teng")
#1ning kvadrati 1 ga teng
#2ning kvadrati 4 ga teng
#3ning kvadrati 9 ga teng
#4ning kvadrati 16 ga teng
#5ning kvadrati 25 ga teng
#6ning kvadrati 36 ga teng
#7ning kvadrati 49 ga teng
#8ning kvadrati 64 ga teng
#9ning kvadrati 81 ga teng
#10ning kvadrati 100 ga teng
sonlar = list(range(1,11))
sonlar_kv = []
for son in sonlar:
    sonlar_kv.append(son**2)
print(sonlar)
print(sonlar_kv)
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  




