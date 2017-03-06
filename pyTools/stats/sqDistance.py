# -*- coding: utf-8 -*-

'''
Efficiently compute squared euclidean distances between sets of vectors
Compute the squared Euclidean distances between every d-dimensional point
in p to every d-dimensional point in q. Both p and q are
npoints-by-ndimensions. 

d(i, j) = sum((p(i, :) - q(j, :)).^2)s

pSOS = sum(p.^2, 2) and is calculated if not specified
qSOS = sum(q.^2, 2) and is calculated if not specified

'''

import numpy as np

def sqDistance(p, q, pSos = None, qSos = None):

    if not pSos:
        pSos = (p*p).sum(1).reshape(-1,1)
    if not qSos:
        qSos = (q*q).sum(1).reshape(1,-1)
        
    oneMatrix = np.ones((p.shape[0], q.shape[0]))
    
    d =  pSos*oneMatrix + qSos*oneMatrix - 2*p.dot(q.T)
    
    return d
