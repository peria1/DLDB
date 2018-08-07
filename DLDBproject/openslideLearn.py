# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:54:47 2018

@author: William
"""
#import tkinter as tk
#import tkFileDialog
#
#print(tkFileDialog.askopenfilename())
#
#import tk
#from tk.filedialog import askopenfilename
#tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)

#
# the following 5 lines will pop up a file chooser window. Five lines!! HA!
#
import tkinter as tk
from tkinter.filedialog import FileDialog
root = tk.Tk()
root.withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = tk.filedialog.askopenfilename()
print(filename)