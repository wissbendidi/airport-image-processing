import numpy as np
import cv2


def seuil(im, s):
    im_s = np.zeros_like(im)
    im_s[im >= s]=255
    return im_s


def myseuil_interactif(im):
    global seuil1

    def myseuil_interactif_callback(val):
        global seuil1
        seuil1=val
        cv2.imshow('Interactive Threshold', seuil(im, seuil1))

    cv2.namedWindow('Interactive Threshold')
    cv2.createTrackbar('Threshold', 'Interactive Threshold', 100, 256, myseuil_interactif_callback)
    myseuil_interactif_callback(100)

    cv2.waitKey(0)
    cv2.destroyWindow('Interactive Threshold')
    return seuil1