"""
split zed camera image to left image and right image.
eg: img[0:h, 0:w, : ] --> leftimg[0:h, 0:int(w/2), : ] and rightimg[0:h, int(w/2+1):w, : ].
"""

import cv2
import os

if __name__ == "__main__":
    path = "C:\\Users\\huadong\\Pictures\\photo"   # change this dirpath.
    listdir = os.listdir(path)
    
    newdir = os.path.join(path, 'split')    # make a new dir in dirpath.
    if(os.path.exists(newdir) == False):
        os.mkdir(newdir)
        
    for i in listdir:
        if i.split('.')[1] == "jpg":	# the format of zed img.
            filepath = os.path.join(path, i)
            filename = i.split('.')[0]
            leftpath = os.path.join(newdir, filename) + "_left.jpg"
            rightpath = os.path.join(newdir, filename) + "_right.jpg"

            img = cv2.imread(filepath)
            [h, w] = img.shape[:2]
            print(filepath, (h, w))
            limg = img[:, :int(w/2), :]
            rimg = img[:, int(w/2+1):, :]

            cv2.imwrite(leftpath, limg)
            cv2.imwrite(rightpath, rimg)

