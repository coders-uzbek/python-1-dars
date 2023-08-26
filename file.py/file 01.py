# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:42:46 2023

@author: Quvonchbek
"""
with open("pi.txt") as file:
    pi = file.read()

print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", "")
pi = float(pi)
print(pi)


filename = "data/talabalar.txt"
with open(filename) as file:
    for line in file:
        print(line)

with open(filename) as file:
    talabalar = file.readlines()

print(talabalar)

