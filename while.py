# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 08:25:36 2023

@author: Quvonchbek
"""
ism = input("Ismingiz nima? ")
print(f'Salom, {ism.title()}')

ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
# Ismingiz nima? Quvonchbek
# Salom, Quvonchbek. Yoshingiz nechida? 15
ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
yosh = int(yosh)
boy = input("Bo'yingiz necha metr? ")
boy = float(boy)
#Ismingiz nima? Quvonchbek
#Salom, Quvonchbek. Yoshingiz nechida? 15
#Bo'yingiz necha metr? 1.52
son = 0
while son<=6:
    print(son,end=' ')
    son = son+1
# 0 1 2 3 4 5 6 
print("Sonni kv.ratini ko'rsatuvchi dastur")
savol= "istalgan sonni kiriting"
savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
if qiymat != 'exit':
    print(float(qiymat)**2)
    
print("Sonni kv.ratini ko'rsatuvchi dastur")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)
        
print("Sonni kv.ratini ko'rsatuvchi dastur")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**2)
        
sonlar = list(range(1,10))
for son in sonlar: 
    if son == 6: # son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son**2} ga teng")
# 1 ning kvadrati 1 ga teng
# 2 ning kvadrati 4 ga teng
#3 ning kvadrati 9 ga teng
# 4 ning kvadrati 16 ga teng
# 5 ning kvadrati 25 ga teng

sonlar = list(range(1,10))
for son in sonlar:
    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
        continue
    print(f"{son} ning kvadrati {son**2} ga teng")
# 1 ning kvadrati 1 ga teng
# 2 ning kvadrati 4 ga teng
# 3 ning kvadrati 9 ga teng
# 4 ning kvadrati 16 ga teng
# 6 ning kvadrati 36 ga teng
# 7 ning kvadrati 49 ga teng
# 8 ning kvadrati 64 ga teng
# 9 ning kvadrati 81 ga teng

son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)
# cheksiz davom etadi

        
        
    
    
 



