# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:56:50 2018

@author: Bill
"""

import numpy as np
import lmdb
import caffe

env = lmdb.open('mylmdb', readonly=True)
with env.begin() as txn:
    raw_datum = txn.get(b'00000000')

datum = caffe.proto.caffe_pb2.Datum()
datum.ParseFromString(raw_datum)

flat_x = np.fromstring(datum.data, dtype=np.uint8)
x = flat_x.reshape(datum.channels, datum.height, datum.width)
y = datum.label