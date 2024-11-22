author = "Wissal Bendidi"

import numpy as np
from operator import itemgetter
import math

#Function used to build a structuring element
#You need to choose the type (disk, square, diamond, line)
#Then give the size and, in the case of the line, the angle
#The structuring element is returned as a list of coordinates
def build_as_list(type, size, angle):
    if type in ['disque', 'disk']:
        Strel = [] #The result will be a list of coordinates
        #Scan all x and y coordinates from -size to size to test if the pixel is at a distance less than size of the center.
        #If yes, add the pixel to the list
        for x in range(-((int)(size))-1,((int)(size))+2):
            for y in range(-((int)(size))-1,((int)(size))+2):
                if( (abs(x)-0.5)*(abs(x)-0.5) + (abs(y)-0.5)*(abs(y)-0.5) <= size*size ):
                    Strel.append((y,x))

    elif type in ['carre', 'square']:
        #Put in the result all coordinates between -size and size included
        Strel = [(y,x) for x in range(-size, size+1) for y in range(-size, size+1)]

    elif type in ['diamant', 'diamond']:
        #Scan all lines from -size to size, and add the coordinates that belong to the diamond
        Strel = [(i,j) for i in range(-size,size+1) for j in range(-size+abs(i), size-abs(i)+1)]


    elif type in ['ligne', 'line']:
        Strel = []
        d=size
        a=angle

        #In case angle is not in [-90;90], bring it back in this interval
        while (a > 90):
            a = a - 180
        while (a < -90):
            a = a + 180
        #Then, if the angle is greater than 45deg, we subtract 90deg and will rotate after the result
        rot=0
        if (a>45):
            a = a-90
            rot=1
        elif (a<-45):
            a = a+90
            rot=3;
        #Convert angle in radian
        a=a*math.pi/180
        #Do this to convert the angle for the left bottom corner of the image
        a=-a

        #Calcuate the size of the structuring element regarding the size
        lx = int(math.ceil(d/math.sqrt(1+math.tan(a)*math.tan(a))))
        if(lx==0):
            lx = 1
        ly = int(math.ceil(d*math.tan(abs(a))/math.sqrt(1+math.tan(a)*math.tan(a))))
        if(ly==0):
            ly = 1

        #result allocation
        Strel = []

        #Bresenham algorithm
        for x in range(-lx,lx+1):
            y = math.tan(a)*x;
            Strel.append((int(round(y)), x))

        #If we need to rotate the result
        if(rot>0):
            #We rotate with a transposition and horizontal flip
            for i in range(0, len(Strel)):
                Strel[i] = (-Strel[i][1], Strel[i][0])

    else:
        assert(False), type+" is not a valid name for a structuring element."


    return Strel

	
	

#This function will return a structuring element as an image
#You need to choose the type (disk, square, diamond, line)
#Then give the size and, in the case of the line, the angle
#The structuring element is returned as an image
def build(type, size, angle=None):
	return toImage(build_as_list(type, size, angle))



#This function takes a list of coordinates as an input, and returns a binary image with the coordinates painted in white
def toImage(Strel):
    if len(Strel) == 0:
        assert (False), "The structuring element is empty."

    #Find the bounding box of the structuring element
    max_i = max(Strel, key=itemgetter(0))[0]
    min_i = min(Strel, key=itemgetter(0))[0]
    max_j = max(Strel, key=itemgetter(1))[1]
    min_j = min(Strel, key=itemgetter(1))[1]


    #build output image
    Im = np.zeros([max_i-min_i+1, max_j-min_j+1, 1], np.uint8)

    for (i,j) in Strel:
        Im[i+abs(min_i), j+abs(min_j)] = 255

    return Im


