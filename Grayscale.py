import cv2

def grayframe(frame):
    #turns image to grayscale
    return(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
