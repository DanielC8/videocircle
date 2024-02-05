import cv2

def initresult(filename,size):
    #prepares file to be written
    result = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'mp4v'),10,size)
    return(result)
def writeframe(frame,result):
    #writes onto file
    result.write(frame)
