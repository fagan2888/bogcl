#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import glob
import utils as utils
import numpy as np
from config import *

plt.style.use("bmh")

pttype = "*"
ncol, nrow = 3, 6
flist = np.array((glob.glob(os.path.join(configs["dpath"], "*", pttype + "*.fits"))))

fnumbers = np.argsort(np.array([int(''.join(filter(str.isdigit, f.split("/")[-1]))) for f in flist]))

flist=flist[fnumbers]


fig, ax = plt.subplots(nrow, ncol, figsize=[5, 7])
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.05, 0.25)



for ii in range(nrow):
    ind = ncol * ii    
    tempset = np.sort(flist[ind:ind+3])
    for jj in range(ncol):
        ax[ii, jj].axis("off")
        ax[ii, jj].imshow(utils.fits2stamp(tempset[jj]))
        ax[ii, jj].set_title(os.path.split(tempset[jj])[-1], fontsize=10)
plt.show()
