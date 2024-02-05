import cv2

def puttingcircle(frame,x,y,radius,color,thickness):
    #adds a circle
    cv2.circle(frame, (x, y), radius, color, thickness)
