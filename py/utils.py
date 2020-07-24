#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import glob
import pandas as pd
from astropy.io import fits
from config import *


def get_file_list(stype=None, imtype="gif", verbose=False):
    """
    Get the file list.
    """

    # -- set the search path
    srch = os.path.join(configs["dpath"], "*", "*", "*." + imtype)

    # -- get the file list
    flist = sorted(glob.glob(srch))

    # -- print pre-filtered file list if desired
    if verbose:
        print("pre-filtered file list: {0}".format(flist))

    # -- filter and return
    if stype is not None:
        return [i for i in flist if stype in i]
    else:
        return flist


def fits2stamp(fname):
    """
    Pull the postage stamp from a fits file.
    (MAKES ASSUMPTIONS ABOUT FITS HDU LAYOUT)

    Returns:
        numpy.ndarray
    """

    return fits.open(fname)[0].data


def labels_csv2feather():
    """
    Write labels csv to feather.
    """

    # -- define the labels name
    lname = os.path.join(configs["lpath"], "autoscan_features.3.csv")

    # -- read csv
    print("reading {0}...".format(lname))
    labels = pd.read_csv(lname, skiprows=6)

    # -- write feather
    opath = os.path.join("..", "output")
    oname = os.path.split(lname)[-1].replace(".csv", ".feather")
    oname = os.path.join(opath, oname)

    print("writing {0}...".format(oname))
    labels.to_feather(oname)

    return


def get_label_ids(label="bogus"):
    """
    Get the ID for a given label type
    """

    # -- define label types
    ldict = {"real" : 0, "bogus" : 1}

    # -- read in the feather file
    fname = os.path.join("..", "output", "autoscan_features.3.feather")
    feat = pd.read_feather(fname)

    # -- return IDs for a given label (OBJECT_TYPE)
    ind = feat["OBJECT_TYPE"] == ldict[label]

    return feat[ind]["ID"].values


def flist2ids(flist):
    """
    Pull IDs off of list of file locations.
    """

    # -- return IDs as integers
    return [int(re.findall("\d+", os.path.split(i)[-1])[0]) for i in flist]
