#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:42:18 2018

@author: bill
"""
# Does not block...makes plot and prints hello
import matplotlib.pyplot as plt
plt.figure('Close me to get hello')
plt.plot(0,0,'*')
plt.show()

print("hello")

#-------------
# Blocks! Makes plot and waits for user to close, then prints hello. 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.figure('Close me to get hello')
plt.plot(0,0,'*')
plt.show()

print("hello")
