# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:33:20 2018

@author: Bill Peria
"""
import numpy as np
import pickle
import lmdb
import sys
import matplotlib.pyplot as plt
#
# toy version of the database. The catalog of whole-slide images is reduced to a list of file names, and the tiles array is nothing but 2D arrays of random numbers in a list. Actually, I guess literally any Python object could be stuffed into the fields of dldb. Weird. 

class dldb:
    def __init__(self,cat,dat):
        self.sourceCatalog = cat
        self.tiles = dat
        print('Built it!')
    def getCatalog(self):
        return self.sourceCatalog
    
#-----------------
# build pretend dldb
#
files = ['wsi1.svs','wsi2.svs','wsi.3svs','wsi4.svs']
imgl = []
for i in range(len(files)):
    imgl.append(np.random.chisquare(i+1,size=(100,100)))
 
dldbfake = dldb(files,imgl)   # did not try to lmdb this yet. Instead, I did each field separately, as pickled byte strings. So my class definition is just a facade for now. 
 
cat2save = pickle.dumps(files)
tiles2save = pickle.dumps(imgl)

#map_size = sys.getsizeof(tiles2save, None)*10
 
rambytes = 1024 * 1024 *1024 * 64 # 64 gigabytes
num2fillRAM = int(np.ceil(rambytes/imgbytes))
map_size = rambytes * 10

env = lmdb.open('tilesOplenty', map_size=1e9, integerkey=True)
nimgl = len(imgl)
nimg2write = 100
with env.begin(write=True) as txn:
    cursor = txn.cursor()
    for i in range(nimg2write):
        txn.put(str(i).encode(), pickle.dumps(imgl[i % nimgl]))
        if (i%10000 == 0):
            print(str(i))
#    txn.put('catalog'.encode(), cat2save) # txn is a Transaction object
#    txn.put('tiles'.encode(), tiles2save) 
env.close()

env = lmdb.open('tilesOplenty', map_size=map_size)
ranpick = 400001
imgchk = []
with env.begin(write=False) as txn:
    for i in range(13):
        imgchk.append(pickle.loads(txn.get(str(ranpick+i).encode())))
env.close()
showImages(imgchk)

#env = lmdb.open('mylmdb', map_size=map_size)
#with env.begin(write=False) as txn:
#    catalogCheck = pickle.loads(txn.get(b'catalog'))
#    tilesCheck = pickle.loads(txn.get(b'tiles'))
#    cursor = txn.cursor()
#    print(cursor.last())
#    print(cursor.key())
#    cursor.first()
#    print(cursor.key())
#    print(env.stat())
#env.close()

print(files)
print(catalogCheck)

def showImages(imglist): # make rows of 4
    fig=plt.figure(figsize=(16,16))
    columns = 4
    rows = int(len(imglist)/columns + 1)
    for i in range(len(imglist)):
        fig.add_subplot(rows,columns,i+1)
        plt.imshow(imglist[i])
    plt.show() 

#---------------------------   
""" 

  I found the following by googling to see how I could access one image at a 
 time. Before starting this, I thought that lmdb would let me make a GIANT array, i.e. too big to fit in RAM. 
 
  But as I've done things here, the lmdb contains only two entries, and I am unpickling each of them, via pickle.loads(), in their entirety. That seems to defeat the purpose. I doubt if pickle is doing mapped-memory. So if my "list of tiles" is 150 GB, I bet what I'm doing above here will fail. 
  
  How can I save a kajillion images into mapped-memory storage via lmdb. 
 
 
"""
num_entries = 0
with lmdb.open('mylmdb', map_size=500e9).begin(
        write=False).cursor() as cursor:
    cursor_iterator = cursor.iternext()
    for _, _ in cursor_iterator:
        num_entries += 1
print(num_entries)
    
#class dldb:
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#    def getx(self):
#        return self.x
