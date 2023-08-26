# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:46:08 2023

@author: Quvonchbek
"""
import pickle

with open("info", "rb") as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)
