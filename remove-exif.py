#!/usr/bin/env python


import sys
import piexif
from PIL import Image


def isJPEG(filename):
    try:
        img = Image.open(filename)
        return img.format == 'JPEG'
    except IOError:
        return False


for arg in sys.argv[1:]:
    if isJPEG(arg) == True:
        piexif.remove(arg)
        print(arg + ' -> has been removed Exif.')
    else:
        print(arg + ' -> is not a JPEG image!')
