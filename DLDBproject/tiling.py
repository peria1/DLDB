# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:01:26 2018

@author: lboucher
"""

# Uncomment all the commented code lines below if you want to visualize the 
# tiles as they are extracted.

import openslide
import numpy as np
import scipy as sp
#import matplotlib.pyplot as plt
import skimage.transform
import glob

#plt.ion() # uncomment for visualization
input_directory = 'data/' # define directory where the .svs files live
output_directory = 'data/tiles/' # define directory where you want the tiles

filenames = sorted(glob.glob(input_directory+'*.svs'))

for filename in filenames: # loop over all svs files
    I = openslide.open_slide(filename) # read in current file
    level_dims = I.level_dimensions # for use later
    level_downs = I.level_downsamples # not used now ,but probably should to
                                      # avoid hard-coded values below

    #J_whole = np.asarray(I.read_region((0,0),3,level_dims[3])) # uncomment for viz
    
    cnt = 0 # to keep track of tile number
    
    # loop over first dimension of image (second dim per OpenSlide's insistence
    # on doing it backwards)
    for m in range(0,level_dims[1][1],299):
        # loop over second dimension (first dim according to OpenSlide)
        for n in range(0,level_dims[1][0],299):
            # check that there's enough pixels left for 299*2x299*2 pixels
            if (m+299*2<level_dims[1][1]) & (n+299*2<level_dims[1][0]): 
                # read 299*2x299*2 region from whole-slide image
                J = np.asarray(I.read_region((n*4,m*4),1,(299*2,299*2)))
                # compute mean pixel value to ignore non-tissue
                int_mean = J[:,:,0:2].mean()
                # arbitrary decisiont to use 224--seems to keep most tissue
                if int_mean<224:
                    cnt = cnt+1 # increment tile count
                    # resize to 299x299
                    J_resize = skimage.transform.resize(J,(299,299))
                    # print some status/info stuff so you know things are happening
                    print((m,n,cnt,int_mean)) 
                    
                    # uncomment following code block for visualization
                    #plt.figure(1)
                    #plt.hold(False)
                    #plt.clf()
                    #plt.imshow(J_whole)
                    #plt.hold(True)
                    #plt.plot([n/16,n/16],[m/16,m/16+299*2/16],'g-')
                    #plt.plot([n/16+299*2/16,n/16+299*2/16],[m/16,m/16+299*2/16],'g-')
                    #plt.plot([n/16,n/16+299*2/16],[m/16,m/16],'g-')
                    #plt.plot([n/16,n/16+299*2/16],[m/16+299*2/16,m/16+299*2/16],'g-')
                    #plt.pause(0.01)
                    #plt.figure(2)
                    #plt.clf()
                    #plt.imshow(J_resize)
                    #plt.pause(0.01)
                    
                    # save the tile as jpg
                    sp.misc.imsave(output_directory+filename[5:-4]+'_'+\
                        str(cnt)+'.jpg',J_resize)
        