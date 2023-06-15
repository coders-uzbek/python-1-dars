# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 06:05:43 2023

@author: Quvonchbek
"""


car0 = {
    "model": "lacetti",
    "rang": "oq",
    "yil": 2020,
    "narh": 13000,
    "km": 50000,
    "korobka": "avtomat",
}

car1 = {
    "model": "nexia 3",
    "rang": "qora",
    "yil": 2018,
    "narh": 9000,
    "km": 89000,
    "korobka": "mexanika",
}

car2 = {
    "model": "gentra",
    "rang": "qizil",
    "yil": 2022,
    "narh": 15000,
    "km": 20000,
    "korobka": "mexanika",
}
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")

# print(cars[0]['model'])

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

malibus = []
for n in range(10):
    new_car = {
        "model": "malibu",
        "rang": None,  # rangi noaniq
        "yil": 2020,
        "narh": None,
        "km": 0,
        "korobka": "avto",
    }
    malibus.append(new_car)

# for malibu in malibus:
# print(malibu)

for malibu in malibus[:3]:
    malibu["rang"] = "qizil"

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[3:6]:
    malibu["rang"] = "qora"

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[6:]:
    malibu["rang"] = "qora"
    malibu["korobka"] = "mexanika"

# for malibu in malibus:
#     print(malibu)

for malibu in malibus:
    if malibu["korobka"] == "avto":
        malibu["narh"] = 40000
    else:
        malibu["narh"] = 35000

for malibu in malibus:
    print(malibu.values())   
    dasturchilar = {
    "ali": ["python", "c++"],
    "vali": ["html", "css", "js"],
    "hasan": ["php", "sql"],
    "husan": ["python", "php"],
    "maryam": ["c++", "c#"],
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end="")
    for til in tillar:
        print(f"{til.upper()} ", end="")
    
    hamkasblar = {
    "ali": {
        "familiya": "valiyev",
        "tyil": 1995,
        "malumot": "oliy",
        "tillar": ["python", "c++"],
    },
    "vali": {
        "familiya": "aliyev",
        "tyil": 2001,
        "malumot": "o'rta-maxsus",
        "tillar": ["html", "css", "js"],
    },
    "hasan": {
        "familiya": "husanov",
        "tyil": 1999,
        "malumot": "maxsus",
        "tillar": ["python", "php"],
    },
}

for ism, info in hamkasblar.items():
    print(
        f"\n{ism.title()} {info['familiya'].title()}, "
        f"{info['tyil']}-yilda tug'ilgan. "
        f"Ma'lumoti: {info['malumot']}. \n"
        "Quyidagi dasturlash tillarini biladi:"
    )
    for til in info["tillar"]:
        print(til.upper(), end=" ")
