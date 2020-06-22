# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:36:31 2019

@author: Lenovo
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


veriler=pd.read_csv('maaslar.csv')
print(veriler)


x=veriler.iloc[:,1:2]
y=veriler.iloc[:,2:]
X=x.values
Y=y.values
#linear regression
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,Y)#values lar iki ayrı değişkende tutulabilir
#ör:X=x.values gibi

plt.scatter(X,Y,color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.show()

#Polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(X)
print(x_poly)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color='red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color='blue')
plt.show()


poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(X)
print(x_poly)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y,color='red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color='blue')
plt.show()

#tahminler
#print(lin_reg.predict(11))
#print(lin_reg.predict(6.6))

print(lin_reg2.predict(poly_reg.fit_transform(11)))
print(lin_reg2.predict(poly_reg.fit_transform(6.6)))


#verilerin ölçeklenmesi
from sklearn.model_selection import StandardScaler

sc1=StandardScaler()
x_olcekli=sc1.fit_transform(X)
sc2=StandardScaler()
y_olcekli=sc2.fit_transform(y)

from sklearn.svm import SVR
svr_reg=SVR(kernel='rbf')
svr_reg.fit(x_olcekli,y_olcekli)

plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color='blue')

print(svr_reg.predict(11))
print(svr_reg.predict(6.6))






