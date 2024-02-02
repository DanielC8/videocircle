import cv2
import numpy as np
from Grayscale import *
from GaussianBlur import *
from CannyEdge import *
from HoughCircleDetection import *
from PutCircle import *
def ImageProcess(frame):
    # Turns into grayscale
    gray = grayframe(frame)

    # Gaussian Blur
    gaussian = Gaussian(gray,15,15,0)

    # gets all the edges
    cannyedge = CannyDetection(gaussian,5,30)

    # hough circles
    circles = HoughCircle(cannyedge,1.2,9999,110,60,0,90)
    # loops through the circles
    if circles is not None:
        circlelist = np.uint16(np.around(circles))
        # generates a circle and center dot for each circle
        for circle in circlelist[0, :]:
            x, y, radius = circle
            # draws the circlel
            puttingcircle(frame,x,y,radius,(0, 255, 20), 5)

            # draw a dot at the center
            cv2.circle(frame, (x, y), 1, (0, 255, 20), 10)
    return(frame)
