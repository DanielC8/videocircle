import cv2
import numpy as np



def ImageProcess(frame)
    # Turns into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gaussian Blur
    gaussian = cv2.GaussianBlur(gray, (15, 15), 0)

    # gets all the edges
    cannyedge = cv2.Canny(gaussian, 5, 30)

    # hough circles
    circles = cv2.HoughCircles(cannyedge, cv2.HOUGH_GRADIENT, 1.2, 9999, param1=110, param2=60, minRadius=0, maxRadius=90)
    # loops through the circles
    if circles is not None:
        circlelist = np.uint16(np.around(circles))
        # generates a circle and center dot for each circle
        for circle in circlelist[0, :]:
            x = circle[0]
            y = circle[1]
            radius = circle[2]
            # draws the circlel
            cv2.circle(frame, (x, y), radius, (0, 255, 20), 5)

            # draw a dot at the center
            cv2.circle(frame, (x, y), 1, (0, 255, 20), 10)
    return(frame)
