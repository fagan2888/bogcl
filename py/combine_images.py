#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import glob
import numpy as np
from config import *
import utils as utils

def prepload(extension='fits'):

    
    flist = np.array((glob.glob(os.path.join(configs["dpath"], "*", "*." + extension))))

    imlist_dict = {}
    imlist_dict["fnumbers"] = np.argsort(np.array([int(''.join(filter(str.isdigit, f.split("/")[-1]))) for f in flist]))

    imlist_dict["flist"] = flist[imlist_dict["fnumbers"]]
    imlist_dict["nimgs"] = imlist_dict["fnumbers"].shape[0]
    imlist_dict["nobjects"] = np.unique(imlist_dict["fnumbers"])


    if imlist_dict["nimgs"] % 3 :
        print("warning: images not in triplets")
        return np.nan
    print(imlist_dict["flist"][0])
    imlist_dict["imshp"] = utils.fits2stamp(imlist_dict["flist"][0]).shape
    
    return imlist_dict


def loadbatch(extension="fits"):
    imdict = prepload(extension)
    assert(isinstance(imdict, dict))
    
    imges = np.zeros((imdict["fnumbers"].shape[0], 3,
                      imdict["imshp"][0],
                      imdict["imshp"][1]), np.uint8)

    for i,ni in enumerate(range(imdict["nimgs"])[::3]):
        tempset = np.sort(imdict["flist"][ni:ni+3])
        for j in range(3):
            imges[i,j] = plt.imread(tempset[j])
            


    return imges
