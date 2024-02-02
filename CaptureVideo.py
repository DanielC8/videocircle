import cv2

def CaptureVid(videoname):
    #get video from camera
    video = cv2.VideoCapture(videoname)
    return(video)