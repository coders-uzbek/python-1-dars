# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 13:56:56 2023

@author: Quvonchbek
"""
faylnomi = 'new_file.txt'
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
    
    
with open(faylnomi,'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')