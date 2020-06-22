# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 20:19:22 2019

@author: Lenovo
"""
import numpy as np
A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)