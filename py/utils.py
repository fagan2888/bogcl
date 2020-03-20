#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import pandas as pd
from astropy.io import fits
from config import *


def get_file_list(stype=None, imtype="gif"):
    """
    Get the file list.
    """

    srch = os.path.join(configs["dpath"], "*", "*." + imtype)
    flist = sorted(glob.glob(srch))

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


# def read_labels():
#     """
#     Read the labels file.
#     """

#     return 0
