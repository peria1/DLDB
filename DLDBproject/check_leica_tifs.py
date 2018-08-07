#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 07:29:21 2018

@author: bill
"""

import openslide
import numpy as np
#import scipy as sp
import skimage.transform
import glob
import lmdb
import pickle
import os
#import sys
import matplotlib.pyplot as plt
import platform as platf
import time
import imageio
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('checktiffs.pdf')

def tmpchoosedir(): # not even kidding
    import tkinter as tk
    from tkinter.filedialog import FileDialog
    root = tk.Tk()
    root.focus_force()
    root.withdraw() # we don't want a full GUI, so keep the root window 
                        #  from appearing
    pathname = tk.filedialog.askdirectory()
    return pathname

def tmpget_slash():
    if platf.system() == 'Windows':
        slash = '\\' # So pythonic!! Duplicit is better than complicit. 
    else:
        slash = '/'
    return slash


file_type = '*.tif'  # someday this will have other possible values
newSourceImages = sorted(glob.glob(tmpchoosedir() + tmpget_slash() + file_type))
type(newSourceImages)
#newSourceImages = newSourceImag7es[0:2]
type(newSourceImages)

for tiffile in newSourceImages:
    print(tiffile)
    Itest = openslide.open_slide(tiffile)
    try:
        imgtest = np.asarray(Itest.read_region((0,0),0,Itest.dimensions))
        for i in range(imgtest.shape[2]):
            plt.figure(i)
            plt.clf()
            plt.imshow(imgtest[:,:,i])
            plt.title(tiffile.split(sep=tmpget_slash())[-1] + ': '+ str(i))
            pp.savefig()
    except Exception as e:
        plt.figure(i)
        plt.clf()
        plt.title(tiffile.split(sep=tmpget_slash())[-1] + ': '+ str(i) +': \n' + str(e))
        pp.savefig()
        #plt.text(0,Itest.dimensions[1]/2,str(e))

        
            
            
pp.close()