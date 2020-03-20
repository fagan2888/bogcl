#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from utils import *


# -- get the file list of difference images
flist = get_file_list("diff")


# -- read in the first 1000
nimg  = 1000
imgs  = np.array([plt.imread(i).astype(float) for i in flist[:nimg]])
imgs /= imgs.max()


# -- PCA decomposition
nrow     = imgs.shape[1]
ncol     = imgs.shape[2]
xx_imgs  = imgs.reshape(nimg, nrow * ncol).copy()
xx_imgs -= xx_imgs.mean(axis=1, keepdims=True)
xx_imgs /= xx_imgs.std(axis=1, keepdims=True)

pca = PCA(n_components=9)
pca.fit(xx_imgs)


# -- view the components
fig, ax = plt.subplots(3, 3, figsize=[7, 7])

for ii in range(3):
    for jj in range(3):
        ind = ii * 3 + jj

        ax[ii, jj].imshow(pca.components_[ind].reshape(nrow, ncol))

plt.show()


# -- project
coeffs = pca.transform(xx_imgs)


# -- cluster PCA components
km = KMeans(n_clusters=5)
km.fit(coeffs)

