#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
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
