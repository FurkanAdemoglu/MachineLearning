# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:01:12 2019

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler=pd.read_csv('odev_tenis.csv')
print(veriler)

outlook=veriler.iloc[:,0:1].values
print(outlook)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
outlook[:,0]=le.fit_transform(outlook[:,0])
print(outlook)
ohe=OneHotEncoder(categorical_features='all')
outlook=ohe.fit_transform(outlook).toarray()


windy=veriler.iloc[:,3:4].values
print(windy)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
windy[:,0]=le.fit_transform(windy[:,0])
print(windy)
ohe=OneHotEncoder(categorical_features='all')
windy=ohe.fit_transform(windy).toarray()

play=veriler.iloc[:,-1:].values
print(play)
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
play[:,0]=le.fit_transform(play[:,0])
print(play)
ohe=OneHotEncoder(categorical_features='all')
play=ohe.fit_transform(play).toarray()

sonuc=pd.DataFrame(data=outlook,index=range(14),columns=['overcast','rainy','sunny'])
print(sonuc)

sonuc2=pd.DataFrame(data=windy,index=range(14),columns=['false','true'])
print(sonuc2)

sonuc3=pd.DataFrame(data=play,index=range(14),columns=['No','Yes'])
print(sonuc3)

s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print(s2)

s3=pd.concat([s2,veriler.iloc[:,1:3]],axis=1)
print(s3)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(s3.iloc[:,1:2],s3.iloc[:,-1:],test_size=0.33,random_state=0)



from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)
print(y_pred)

import statsmodels.formula.api as sm
X=np.append(arr=np.ones((14,1)).astype(int),values=s3.iloc[:,:-1],axis=1)
X_l=s3.iloc[:,1].values
r_ols=sm.OLS(endog=s3.iloc[:,-1:],exog=X_l)
r=r_ols.fit()
print(r.summary())

'''X_l=s3.iloc[:,[0,1,2,3,5]].values
r_ols=sm.OLS(endog=boy,exog=X_l)
r=r_ols.fit()
print(r.summary())
'''
y_pred=regressor.predict(x_test)





