# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 15:58:09 2023

@author: Quvonchbek
"""
from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(bemor)
pprint(bemor)
