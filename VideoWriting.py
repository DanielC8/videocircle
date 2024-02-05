import cv2

def initresult(filename,size):
    result = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'mp4v'),10,size)
    return(result)
def writeframe(frame,result):
    result.write(frame)
