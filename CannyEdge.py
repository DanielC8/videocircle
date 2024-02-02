import cv2

def CannyDetection(frame,min,max):
    return(cv2.Canny(frame, min, max))
