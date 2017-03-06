# -*- coding: utf-8 -*-



import scipy.io as sio

def loadData(dataset):
    sio.loadmat('{}.mat'.format(dataset))
    
