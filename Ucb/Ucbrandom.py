# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:20:35 2019

@author: Lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler=pd.read_csv('Ads_CTR_Optimisation.csv')
#print(veriler)
#Random selection
import random

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



































