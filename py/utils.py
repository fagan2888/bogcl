#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from config import *

def get_file_list(imtype=None):
    """
    Get the file list.
    """

    flist = sorted(glob.glob(os.path.join(configs["dpath"], "*", "*.gif")))

    if imtype is not None:
        return [i for i in flist if imtype in i]
    else:
        return flist
