# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 07:35:31 2023

@author: DELL
"""
#car = {'model':'tesla','rang':'qora'}
#print(car['model'])
#print(car['rang'])
# tesla
# qora
talaba = {'ism':'quvonchbek','yosh':15,'t_yil':2008}
print(f"{talaba['ism'].title()},\
      {talaba['yosh']}yoshda,\
    {talaba['t_yil']}-tug'ilgan")
# Quvonchbek,      15yoshda,          2008 tug'ilgan
# yangi juftlik qo'shish
talaba['kurs'] = 1
talaba['fakultet'] = 'informatika'
print(talaba)
# {'ism': 'quvonchbek', 'yosh': 15, 't_yil': 2008, 'kurs': 1, 'fakultet': 'informatika'}
# bo'sh lug'at
student = {}
student['ism'] = 'Quvonchbek'
student['yosh'] = 15
student['t_yil'] = 2008
print(student)
# {'ism': 'Quvonchbek', 'yosh': 15, 't_yil': 2008}
# qiymatni o'zgartirish
student['ism'] = 'Quvonchbek Sherboboyev'
print(student)
# {'ism': 'Quvonchbek Sherboboyev', 'yosh': 15, 't_yil': 2008}
# qiymatni o'chirish
del student['t_yil']
print(student)
# {'ism': 'Quvonchbek Sherboboyev', 'yosh': 15}
# qatorga bo'lib yozish
cars = {'umar':'audi',
        'temur':'BNW',
        'sarvar':'malibu'
        }
moshina = cars['temur']
print(f"Temurning moshinasi {moshina}")
# Temurning moshinasi BNW
moshina = cars.get('ali','Bu ism mavjud emas!')
print(moshina)
# Bu ism mavjud emas!
moshina = cars.get('temur','Bu ism mavjud emas!')
print(moshina)
# BNW
