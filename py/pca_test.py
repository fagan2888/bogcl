#!/usr/bin/env python
# -*- coding: utf-8 -*-

# reads in 1000 image triplets and decomposes them with 9 PCA components

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from utils import *
import combine_images as ci


# -- get the file list of difference images
flist = get_file_list("diff")


# -- read in the first 1000
nimg  = 1510
ncomp = 100
extension = "fits"
extension = "gif"


ncomp = int(np.sqrt(ncomp))**2

imgs, flist = ci.loadbatch(extension=extension, N=nimg,
                              flist=flist, transpose=True, verbose=True)
nimg = int(len(flist) / 3)
nc = int(np.sqrt(ncomp))
nr = nc
print("images:", nimg)
print("PCA components:", ncomp)
imgs = imgs[:,:,:,0]
imgs = imgs.astype(float) / imgs.max()

# -- PCA decomposition
nrow     = imgs.shape[1]
ncol     = imgs.shape[2]
xx_imgs  = imgs.reshape(nimg, nrow * ncol).copy()
xx_imgs -= xx_imgs.mean(axis=1, keepdims=True)

xx_imgs /= xx_imgs.std(axis=1, keepdims=True)

pca = PCA(n_components=ncomp)
pca.fit(xx_imgs)


# -- view the components
fig, ax = plt.subplots(nr, nc, figsize=[7, 7])

for ii in range(nr):
    for jj in range(nc):
        ind = ii * nc + jj

        ax[ii, jj].imshow(pca.components_[ind].reshape(nrow, ncol))

        ax[ii, jj].axis('off')
plt.show()
plt.plot(pca.explained_variance_ratio_.cumsum())
plt.title("explained variance")
plt.show()

# -- project
coeffs = pca.transform(xx_imgs)

# -- cluster PCA components
km = KMeans(n_clusters=6)
km.fit(coeffs)
fig, ax = plt.subplots(3, 2, figsize=[7, 7])

for ii in range(3):
    for jj in range(2):
        ind = ii * 2 + jj

        ax[ii, jj].plot(km.cluster_centers_[ind])

        ax[ii, jj].axis('off')
plt.show()

fig, ax = plt.subplots(5, 6, figsize=[7, 7])
regenerated = np.dot(coeffs,pca.components_)

regenerated = regenerated.reshape(nimg,51,51)
print("cluster, size")
for ii in range(5):
    print (ii, (km.labels_ == ii).sum())
    for jj in range(6):
        tmp = regenerated[km.labels_ == ii][jj]
        #tmp = imgs[km.labels_ == ii]
        ax[ii, jj].imshow(tmp)#[jj,:,:])

        ax[ii, jj].axis('off')
plt.show()
