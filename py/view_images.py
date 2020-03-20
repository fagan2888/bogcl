#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import glob

plt.style.use("bmh")

flist = glob.glob("../data/stamps_10/stamps/20140807-r946/*.gif")

fig, ax = plt.subplots(5, 5, figsize=[7, 7])
for ii in range(5):
    for jj in range(5):
        ax[ii, jj].axis("off")
        ax[ii, jj].imshow(plt.imread(flist[5 * ii] + jj))
for ii in range(5):
    for jj in range(5):
        ax[ii, jj].axis("off")
        ax[ii, jj].imshow(plt.imread(flist[5 * ii + jj]))
