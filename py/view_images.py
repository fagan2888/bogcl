#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
import glob
from config import *

plt.style.use("bmh")

pttype = "*"

flist = np.array((glob.glob(os.path.join(configs["dpath"], "*", pttype + "*.gif"))))

fnumbers = np.argsort(np.array([int(''.join(filter(str.isdigit, f.split("/")[-1]))) for f in flist]))

flist=flist[fnumbers]


fig, ax = plt.subplots(3, 6, figsize=[7, 7])
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95, 0.05, 0.25)



for ii in range(5):
    for jj in range(5):
        ind = 5 * ii + jj

        ax[ii, jj].axis("off")
        ax[ii, jj].imshow(plt.imread(flist[ind]))
        ax[ii, jj].set_title(os.path.split(flist[ind])[-1], fontsize=10)

plt.show()
