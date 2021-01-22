#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:37:34 2021

@author: ctralie
Numpy Examples
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 6, 8, 1, 7, 3, 4, 72])
print(x[0:-2:3]) # Slicing numpy arrays works just like lists

x = np.arange(10)
x = x + 5 # Element-wise addition
y = np.arange(2, 12)
exponent = x**y
print(x)
print(y)
print(x*y) # Element-wise multiplication in parallel
print(x**y) # Element-wise exponentiation

x = np.arange(-20, 21)
y = x**2 + 1 + 10
plt.plot(x, y)
plt.show()