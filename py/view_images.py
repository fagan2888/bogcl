#!/usr/bin/env python
# -*- coding: utf-8 -*-

# code uses loadimages to read in and plot the images

import os
import matplotlib.pyplot as plt
import glob
import utils as utils
import numpy as np
import combine_images as ci

from config import *

plt.style.use("bmh")

imtype = "fits"
#imtype = "gif"

pttype = "*"

#read in file list
flist = np.array(utils.get_file_list(imtype=imtype))

#sort list
fnumbers = np.argsort(np.array([int(''.join(filter(str.isdigit,
                                                   f.split("/")[-1])))
                                for f in flist]))
flist = flist[fnumbers]

tempset, flist = ci.loadbatch(extension=imtype, N=6,
                              flist=flist, transpose=False, verbose=True)
ncol, nrow = 3, min(6, int(len(flist) / 3))
print(ncol, nrow)

fig, ax = plt.subplots(nrow, ncol, figsize=[5, 7])
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.05, 0.25)

for ii in range(nrow):
    ind = ncol * ii
    
    for jj in range(ncol):
        ax[ii, jj].axis("off")     
        ax[ii, jj].imshow(tempset[ii, jj])            
        ax[ii, jj].set_title(os.path.split(flist[ind + jj])[-1], fontsize=10)
        
plt.show()
