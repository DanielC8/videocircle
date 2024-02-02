import cv2
import numpy as np

def CaptureVid(videoname)
    #get video from camera
    video = cv2.VideoCapture(videoname)
    return(video)