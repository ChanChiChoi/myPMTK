# -*- coding: utf-8 -*-
'''
Compute indices for K-fold cross validaiton
N = num data
K = num folds, if K=N, use leave-one-out CV
[trainfolds{i}, testfolds{i}] = indices of i'th fold
If randomize = 1, we shuffle the indices first
  This is useful in case the data has some special ordering
  such as all the positive examples before the negative ones
  
Example:
 [trainfolds, testfolds] = Kfold(100, 3)
 testfolds{1} = 0:N:3, trainfolds{1} = others
 testfolds{2} = 1:N:3, trainfolds{2} = others
 testfolds{3} = 2:N:3, trainfolds{3} = others
 (last fold gets all the left over so has different length)
'''

import numpy as np

def Kfold(N, K, randomize = 0):

    if randomize:
        np.random.seed(0)
        perm = np.arange(N)
        np.random.shuffle(perm)
    else:
        perm = np.arange(N)
        
    trainfolds, testfold = [], []
    
    for i in range(K):
        ind = list(range(N))
        testfolds.append(perm[ind[i::K]])
        del ind[i::K]
        trainfolds.append(perm[ind])
        
    return trainfolds, testfolds
