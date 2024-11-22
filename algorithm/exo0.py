from fonctions import numpy 
import cv2 
from fonctions import myutil
import math
from fonctions import strel
from fonctions import first_functions



img=cv2.imread ("aeroport1.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
cv2.imshow('hsv',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


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

picture = cv2.imread("aeroport3.png")
picture[contours > 0] = [0,0,255]
cv2.imshow("image", picture)
cv2.waitKey(0)
cv2.destroyAllWindows()