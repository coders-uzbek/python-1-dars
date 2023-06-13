# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 17:23:48 2023

@author: Quvonchbek
"""
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh <= 5 or yosh >= 60:
    print("Kirish bepul")
elif yosh <= 15:
    print("Kirish 5000 so'm")
else:
    print("Kirish 10000 so'm")
harorat = float(input("Harorat nechchi?>>>"))
kun = input("Kun nima?>>>")
if harorat>=30 and kun == 'shanba':  
    print("Qani kettik!")
elif harorat<30 and kun =='shanba':
    print("Bugun bormaymiz!")
else:
    print("Afsus!")
kun = input("Bugun nima kun?>>>")
harorat = float(input("Harorat qanday?>>>"))
if (kun == "shanba" or kun == "yakshanba") and harorat>=30:
    print("Bugun dam olishga boramiz!")
elif harorat<=30 and (kun == "shanba" or kun == "yakshanba"):
    print("Bugun borolmaymiz!")
else:
    print("Afsus!")
# ro'yhatni tekshirishda in metodidan foydalanamiz:
taomlar = ['salat,non,osh,somsa,shashlik']
'qaymoq' in taomlar
# false tamlarda yo'q 
ovqat = input("Nima ovqat yeysiz?>>")
if ovqat in taomlar:
    print("Bu taom bizda bor")
else:
    print("Bu taom bizda yoq!")
# not in metodi
foods = ['osh,manti,somsa,lavash']
'shashlik' in foods
# true foods da yo'q

