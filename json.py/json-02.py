# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 05:35:47 2023

@author: Quvonchbek
"""
import json

filename = "bemor.json"
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))
