# -*- coding: utf-8 -*-
'''
I have transform the original mnistAll.mat into 4 subfiles 
'''
import os
from os.path import join
import h5py
pwd = os.getcwd()

train_images = h5py.File(join(pwd,'mnistAll','train_images.mat'),'r')['train_images'][:]
train_labels = h5py.File(join(pwd,'mnistAll','train_labels.mat'),'r')['train_labels'][:]
test_images = h5py.File(join(pwd,'mnistAll','test_images.mat'),'r')['test_images'][:]
test_labels = h5py.File(join(pwd,'mnistAll','test_labels.mat'),'r')['test_labels'][:]
