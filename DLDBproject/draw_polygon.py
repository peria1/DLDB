#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:33:54 2018

@author: bill
"""

import matplotlib.pyplot as plt
import numpy as np
import openslide
#import scipy as sp
#import skimage.transform
#import glob
#import pickle
#import os
##import sys
#import matplotlib.pyplot as plt
#import platform as platf
#import time
#import imageio
#import pandas as pd



#fig, ax = plt.subplots()
#ax.plot(np.random.rand(10))


# following is to recover from plotlib, after clicking.
# line = ax.get_lines()[-1]
# xd= line.get_xdata()
# yd = line.get_ydata()



def onclick(event):
#    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
#          ('double' if event.dblclick else 'single', event.button,
#           event.x, event.y, event.xdata, event.ydata))
#    print('clicked!',event.button)
#    print(event.xdata,event.ydata)
#
    #
    # PLn to check if event.xdata is None, and if it is, I will take that as a 
    # signal that I should finish off with the current file. And then right-click
    # will just mean to finish off with current tissue segment. 
    if event.xdata == None:
        plt.pause(0.5)
        plt.close()
    
    if event.button == 3:
        xpoly.append(xpoly[0])
        ypoly.append(ypoly[0])
        plt.plot(xpoly,ypoly)
        fig.canvas.draw()
        this_poly = list(zip(np.rint(xpoly).astype(int),np.rint(ypoly).astype(int)))
        print(this_poly)

        xpoly[:] = []
        ypoly[:] = []        
        return
    else:
        xpoly.append(event.xdata)
        ypoly.append(event.ydata)
#        print(len(xpoly))
        if len(xpoly) > 1:
#            print('...about to plot...',xpoly,ypoly)
            plt.plot(xpoly[-2:], ypoly[-2:])
            fig.canvas.draw()
        else:
#            print('first x and y...',xpoly,ypoly)
            plt.plot(xpoly,ypoly,'o')
            fig.canvas.draw()

def uichoosefile():
    import tkinter as tk
    from tkinter.filedialog import FileDialog
    root = tk.Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = tk.filedialog.askopenfilename()
    return filename

if __name__=='__main__':
    
    global xpoly,ypoly,cid
    
    plt.clf()
    
    I = openslide.open_slide(uichoosefile())
    level_dims = I.level_dimensions 
                            
    J_whole = np.asarray(I.read_region((0,0),len(level_dims)-1,level_dims[-1]))   
    plt.imshow(J_whole)

    fig = plt.gcf()
    ax = plt.gca()

    xpoly = []
    ypoly = []
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)




