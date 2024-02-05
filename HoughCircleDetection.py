import cv2

def HoughCircle(frame,dp,distance,param1,param2,min,max):
    #hough circle detection
    return(cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, dp, distance, param1=param1, param2=param2, minRadius=min, maxRadius=max))
