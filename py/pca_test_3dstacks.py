#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from utils import *
import combine_images as ci

filetype = ["diff", "search", "template"]

def pcaimgs(imgs):
    
    nimg, nrow, ncol, nchan = imgs.shape
    # -- PCA decomposition
    reshape = (nrow, ncol, nchan)
    xx_imgs  = imgs.reshape(nimg, np.prod(reshape)).copy()
    print (xx_imgs.std(axis=1, keepdims=True))

    xx_imgs -= xx_imgs.mean(axis=1, keepdims=True)
    xx_imgs /= xx_imgs.std(axis=1, keepdims=True)

    pca = PCA(n_components=6)
    pca.fit(xx_imgs)

    return pca, (nrow, ncol, nchan)

def plotpca(pca, theshape):
    nchan = theshape[2]
    nrow = theshape[0]
    ncol = theshape[1]
    
    # -- view the components
    fig, ax = plt.subplots(6, nchan, figsize=[7, 7])

    for ii in range(6):
        for kk in range(nchan):
            ax[ii, kk].axis("off")     
            ax[ii, kk].imshow(pca.components_[
                    ii].reshape(nrow, ncol, nchan).transpose(2,0,1)[kk])
            ax[ii, kk].set_title("PC {} {}".format(ii, filetype[kk]), fontsize=10)


    plt.show()

    
if __name__ == '__main__':

    # -- get the file list of difference images
    flist = get_file_list(imtype="gif")#, verbose=True)
    

    # -- read in the first 1000
    nimg = 1000
    imgs, flist = ci.loadbatch(N=nimg)
    print("N images", imgs.shape)
    print("... doing PCA...")
    
    pca, reshape =  pcaimgs(imgs)
    xx_imgs  = imgs.reshape(nimg, np.prod(reshape))
    
    # -- project
    coeffs = pca.transform(xx_imgs)
    plotpca(pca, reshape)

    # -- cluster PCA components
    km = KMeans(n_clusters=5)
    km.fit(coeffs)
    print (km)

