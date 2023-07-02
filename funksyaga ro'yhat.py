# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:20:57 2023

@author: Quvonchbek
"""
def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
# {'husan': '5', 'hasan': '4', 'vali': '5', 'ali': '5'}

