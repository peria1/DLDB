#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:08:21 2018

@author: bill
"""

import tkinter as tk
def handle_click():
    print('Clicked!')
    root = tk.Tk()
    Button(root, text='Click me', command=handle_click).pack()
    root.mainloop()
