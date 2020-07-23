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
        # read the file list
        flist = np.array(utils.get_file_list(imtype=extension))
        #, verbose=True)

    imlist_dict = {}
    # stores the number that makes the name of each image, e.g. 75605 for srch75605.fits
    imlist_dict["fnumbers"] = np.argsort(np.array([int(
        ''.join(filter(str.isdigit,  f.split("/")[-1])))
                     for f in flist])) 
    # stores the name of the images as a list
    imlist_dict["flist"] = flist[imlist_dict["fnumbers"]]
    # reads only N images - if -1 reads all images
    if N > -1:
        imlist_dict["flist"] = imlist_dict["flist"][:N * 3]
    # checks that the images are in triplets (template, search, difference)
    if imlist_dict["fnumbers"].shape[0] % 3 :
        print("warning: images not in triplets")
        return np.nan
    
    # the total number of triplets
    imlist_dict["nimgs"] = int(imlist_dict["fnumbers"].shape[0] / 3)
    # the list of objects by numbers
    imlist_dict["nobjects"] = np.unique(imlist_dict["fnumbers"])

    # reads in the images choosing method depending on extension
    if extension == "fits":
        imlist_dict["imshp"] = utils.fits2stamp(imlist_dict["flist"][0]).shape
    else:
        imlist_dict["imshp"] = plt.imread(imlist_dict["flist"][0]).shape

    return imlist_dict, imlist_dict["flist"]


def loadbatch(extension="fits", N=-1, flist=None,
              transpose=True, verbose=False):
    imdict, flist = prepload(extension, N=N, flist=None)
    N = int(len(flist) / 3)
    assert(isinstance(imdict, dict))
    if verbose:
        print("N:", N, "extension:", extension)
        print(imdict)
    imdtype = {"fits":float, "gif":np.uint8, }

    # create a container for the images
    imges = np.zeros((N, 3,
                      imdict["imshp"][0],
                      imdict["imshp"][1]), imdtype[extension])
    
    for i, ni in enumerate(range(imdict["nimgs"])[0: N * 3: 3]):
        # sorting diff, search, and template in this order
        imdict["flist"][ni: ni+3] = np.sort(imdict["flist"][ni: ni+3])
        for j in range(3):
            if extension == "fits":
                imges[i,j] = utils.fits2stamp(imdict["flist"][ni:ni+3][j])
            else:
                imges[i,j] = plt.imread(imdict["flist"][ni:ni+3][j])
    if transpose:
        # originally the files are organized in an Nx3x51x51 array;
        # what I want is Nx51x51x3: this is how a color RGB image is organized
        # and I can pass this to a Neural Network
        imges = imges.transpose(0, 2, 3, 1)
    return imges, flist

if __name__ == '__main__':
    loadbatch(verbose=False)
