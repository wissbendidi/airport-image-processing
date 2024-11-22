import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import numpy
from functions import strel
import sys
import math

def my_first_erode(im):
    imr = numpy.zeros_like(im)
    for i in range(1, im.shape[0]-1):
        for j in range (1, im.shape[1]-1):
            imr[i, j] = numpy.amin(im[i-1:i+2, j-1:j+2])
    return imr


def my_first_dilate(im):
    return 255-my_first_erode(255-im)

def myerode(im, E):
    return cv2.erode(im, E)

def mydilate(im, E):
    return cv2.dilate(im, E)

def mygradient(im, E):
    eroded_image = myerode(im, E)
    dilated_image = mydilate(im, E)
    return dilated_image - eroded_image

def myopen(image, E):
    eroded = myerode(image, E)
    opened = mydilate(eroded, E)
    return opened

def myclose(image, E):
    return myerode(mydilate(image, E), E)


def myconddilat(R, M, E):
    dilated = mydilate(M, E)
    return numpy.minimum(dilated, R)


def myconderode(R, M, E):
    eroded = myerode(M, E)
    return numpy.maximum(eroded, R)


def myreconinf(R, M, E):
    old = M
    new = myconddilat(R, old, E)
    while not numpy.array_equal(new, old):
        old = new
        new = myconddilat(R, old, E)
    return new


def myreconsup(R, M, E):
    old = M
    new = myconderode(R, old, E)
    while not numpy.array_equal(new, old):
        old = new
        new = myconderode(R, old, E)
    return new

def myopenreconinf(R, F, E):
    return myreconinf(R, myopen(R,F), E)

def myclosereconsup(R, F, E):
    return myreconsup(R, myclose(R,F), E)


"""tp2

def generate_gradient_images(image_path):
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Unable to open image at {image_path}")
        return None
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    r, g, b = cv2.split(image)

    min_grad = math.inf
    angle_a = 0
    best_gradient_image = None

    for angle in range(-90, 91, 5):
        struct_element = strel.build('line', 40, angle)  
        
        gradient_image = mygradient(r, struct_element)  
        
        grad_sum = numpy.sum(gradient_image)
        
        if grad_sum < min_grad:
            angle_a = angle
            min_grad = grad_sum
            best_gradient_image = gradient_image 

    if best_gradient_image is not None:
        cv2.imshow("Best Gradient Image", best_gradient_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return angle_a

image_path = 'papier_60.png' 
print(generate_gradient_images(image_path))

"""

"""
image = cv2.imread('dog.png')
E= strel.build('disk', 5)
R= cv2.imread('mask_sup.png')

#gradiant_image = dilated_image - eroded_image

cv2.imshow("Image inf1", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Image inf2", myreconsup(image, R, E))
#cv2.imshow("Image gradiant", gradiant_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""