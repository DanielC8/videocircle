import cv2

def puttingcircle(frame,x,y,radius,color,thickness):
    cv2.circle(frame, (x, y), radius, color, thickness)
