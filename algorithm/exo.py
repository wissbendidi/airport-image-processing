import cv2
import numpy 
from functions import myutil
import math
from functions import strel
from functions import first_functions


'''
picture = cv2.imread("text4.png", cv2.IMREAD_GRAYSCALE)
E= strel.build('square', 50)
#image = first_functions.myopen(picture, E)
image = first_functions.myclose(picture, E)
result = image - picture
s= myutil.myseuil_interactif(result)
#s=36
im= myutil.seuil(result, s)

cv2.imshow("image", im)  
cv2.waitKey(0)
cv2.destroyAllWindows()    '''


"""
picture = cv2.imread("rice.png", cv2.IMREAD_GRAYSCALE)
E= strel.build('square', 50)
image = first_functions.myopen(picture, E)
#image = first_functions.myclose(picture, E)
result = picture - image
#s= myutil.myseuil_interactif(result)
s=50
im= myutil.seuil(result, s)
im[:,0] = 0
im[:,-1] = 0
im[0,:] = 0
im[-1,:] = 0

i = 1
image_bin = im.copy()
while numpy.sum(image_bin)!= 0:
    E= strel.build('disk', i)
    image_bin = first_functions.myopen(im, E)
    i+=0.1
t = (i-0.1)*2
print (t)

cv2.imshow("image", first_functions.myopen(im, strel.build('disk', 9.2)))  
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

picture = cv2.imread("images/aeroport2.png", cv2.IMREAD_GRAYSCALE)
angles = numpy.arange(-90, 91, 1)
min_pixel_image = numpy.full(picture.shape, 255, dtype=numpy.uint8)
for angle in angles:
    struct_element = strel.build('line',35, angle)
    image_closed = first_functions.myclose(picture, struct_element)
    min_pixel_image = numpy.minimum(min_pixel_image, image_closed)

#s= myutil.myseuil_interactif(min_pixel_image)


image_bin = myutil.seuil(min_pixel_image, 32)
cv2.imshow("image", image_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_bin1=first_functions.myopen(image_bin, strel.build('square', 2))


image_bin2=first_functions.myclose(image_bin1, strel.build('square', 2))

contours = first_functions.mygradient(image_bin2, strel.build("square", 1))

picture = cv2.imread("aeroport2.png")
picture[contours > 0] = [0,0,255]
cv2.imshow("image", picture)
cv2.waitKey(0)
cv2.destroyAllWindows()