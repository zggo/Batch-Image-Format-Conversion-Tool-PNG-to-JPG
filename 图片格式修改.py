# -*- coding: utf-8 -*-
from PIL import Image
import cv2 as cv
import os

def PNG_JPG(PngPath):
    img = cv.imread(PngPath, 0)
    w, h = img.shape[::-1]
    infile = PngPath
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=100)
            os.remove(PngPath)
        else:
            img.convert('RGB').save(outfile, quality=100)
            os.remove(PngPath)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)

# 转jpg
path_root = os.getcwd()
Path='png2jpg/'
img_dir = os.listdir(Path)
for img in img_dir:
    if img.endswith('.png'):#目标格式
        PngPath= Path + img
        PNG_JPG(PngPath)
img_dir = os.listdir(Path)
for img in img_dir:
    print(img)


# 转png
# i=0
# path = "png2jpg/"
# savepath = "png2jpg/"
# filelist = os.listdir(path)
# for file in filelist:
#     im = Image.open(path+filelist[i])
#     filename = os.path.splitext(file)[0]
#     im.save(savepath+filename+'.png') # or 'test.tif'
#     i=i+1

