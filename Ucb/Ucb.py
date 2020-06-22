# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:20:35 2019

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

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
oduller=[0]*d#ilk başta bütün ilanların odulu 0
toplam=0#toplam odul
secilenler=[]
#Ni(n)
tıklamalar=[0]*d#o anan kadarki tıklamalar
for n in range(1,N):
    ad=0#secilen ilan
    max_ucb=0
    for i in range(0,d):
        if(tıklamalar[i]>0):
            ortalama=oduller[i]/tıklamalar[i]
            delta=math.sqrt(3/2*math.log(n)/tıklamalar[i])
            ucb=ortalama+delta
        else:
            ucb=N*10
        if max_ucb < ucb:#max tan daha büyük bir ucb çıktı
            max_ucb=ucb
            ad=i
    secilenler.append(ad)
    tıklamalar[ad]=tıklamalar[ad]+1
    odul=veriler.values[n,ad]
    oduller[ad]=oduller[ad]+odul
    toplam=toplam+odul
print("Toplam Odul:")
print(toplam)
plt.hist(secilenler)
plt.show()

































