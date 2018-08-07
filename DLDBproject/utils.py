#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 06:33:23 2018

@author: bill
"""

def uichoosefile():
    import tkinter as tk
    from tkinter.filedialog import FileDialog
    root = tk.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = tk.filedialog.askopenfilename()
    return filename
