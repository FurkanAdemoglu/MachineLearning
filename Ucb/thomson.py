# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:20:35 2019

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random
veriler=pd.read_csv('Ads_CTR_Optimisation.csv')
#print(veriler)
#Random selection
'''import random

N=10000
d=10
toplam=0
secilenler=[]
for n in range(0,N):
    ad=random.randrange(d)
    secilenler.append(ad)
    odul=veriler.values[n,ad]#veriler n. satır =1 ise ödül 1
    toplam=toplam+odul

plt.hist(secilenler)
plt.show()
'''
#UCB
N=10000#tıklanma sayısı
d=10#toplam 10 ilan var
#Ri(n)

toplam=0#toplam odul
secilenler=[]
birler=[0]*d
sıfırlar=[0]*d



for n in range(1,N):
    ad=0#secilen ilan
    max_th=0
    for i in range(0,d):
        rasbeta=random.betavariate(birler[i]+1,sıfırlar[i])
        if rasbeta>max_th:
            max_th=rasbeta
            ad=i
    secilenler.append(ad)
    
    odul=veriler.values[n,ad]
    if odul==1:
        birler[ad]=birler[ad]+1
    else:
        sıfırlar[ad]=sıfırlar[ad]+1
    
    toplam=toplam+odul
print("Toplam Odul:")
print(toplam)
plt.hist(secilenler)
plt.show()

































