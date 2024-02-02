import cv2

def Gaussian(frame,dimension1,dimension2,sigma):
    return(cv2.GaussianBlur(frame, (dimension1, dimension2), sigma))
