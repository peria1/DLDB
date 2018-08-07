#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 18:41:57 2018

@author: bill
"""
import matplotlib.pyplot as plt
import numpy as np
import openslide
import DLDB as dl  # argh no that is not how this works. Hoe do I import DLDB so that 
             # my hand segmenter is a subclass or child class of it? Is 
             # subclass and child class the same thing? 


# something like class TissueSeg(DLDB) goes here. The __init__ can basically be pulled 
# from the __main__ bit below.


def onclick(event):
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

        if len(xpoly) > 1:
            plt.plot(xpoly[-2:], ypoly[-2:])
            fig.canvas.draw()
        else:
            plt.plot(xpoly,ypoly,'o')
            fig.canvas.draw()

def GPchoosefile():
    import tkinter as tk
    from tkinter.filedialog import FileDialog
    root = tk.Tk()
    root.withdraw() 
    filename = tk.filedialog.askopenfilename()
    return filename

if __name__=='__main__':
    
    global xpoly,ypoly,cid
    
    plt.clf()
    
    I = openslide.open_slide(GPchoosefile())
    level_dims = I.level_dimensions 
                            
    J_whole = np.asarray(I.read_region((0,0),len(level_dims)-1,level_dims[-1]))   
    plt.imshow(J_whole)

    fig = plt.gcf()
    ax = plt.gca()

    xpoly = []
    ypoly = []
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)




