import cv2

def CannyDetection(frame,min,max):
    #Canny edge detection
    return(cv2.Canny(frame, min, max))
