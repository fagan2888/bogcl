#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import glob
import numpy as np
from config import *
import utils as utils

def prepload(extension='fits', N=-1, flist=None):
    
    if flist is None:
        
        flist = np.array(utils.get_file_list(imtype=extension))#, verbose=True)

    imlist_dict = {}
    imlist_dict["fnumbers"] = np.argsort(np.array([int(
        ''.join(filter(str.isdigit,  f.split("/")[-1])))
                     for f in flist])) 

    imlist_dict["flist"] = flist[imlist_dict["fnumbers"]]
    if N > -1:
        imlist_dict["flist"] = imlist_dict["flist"][:N * 3]

    if imlist_dict["fnumbers"].shape[0] % 3 :
        print("warning: images not in triplets")
        return np.nan

    imlist_dict["nimgs"] = int(imlist_dict["fnumbers"].shape[0] / 3)
    imlist_dict["nobjects"] = np.unique(imlist_dict["fnumbers"])


    if extension == "fits":
        imlist_dict["imshp"] = utils.fits2stamp(imlist_dict["flist"][0]).shape
    else:
        imlist_dict["imshp"] = plt.imread(imlist_dict["flist"][0]).shape

    return imlist_dict, imlist_dict["flist"]


def loadbatch(extension="fits", N=-1, flist=None, transpose=True):
    imdict, flist = prepload(extension, N=N, flist=None)
    assert(isinstance(imdict, dict))
    imdtype = {"fits":float, "gif":np.uint8, }

    imges = np.zeros((N, 3,
                      imdict["imshp"][0],
                      imdict["imshp"][1]), imdtype[extension])

    for i,ni in enumerate(range(imdict["nimgs"])[0:N*3:3]):
        #sorting diff, search and template in this order
        imdict["flist"][ni:ni+3] = np.sort(imdict["flist"][ni:ni+3])
        for j in range(3):
            if extension == "fits":
                imges[i,j] = utils.fits2stamp(imdict["flist"][ni:ni+3][j])
            else:
                imges[i,j] = plt.imread(imdict["flist"][ni:ni+3][j])
    if transpose:
        imges = imges.transpose(0, 2, 3, 1)
    return imges, flist

if __name__ == '__main__':
    loadbatch()
