from FrameProcessing import *
from FrameOutput import *
from VideoWriting import *

def VideoProcessing(video):
    result = initresult("OverlayVideo.mp4",(int(video.get(3)),int(video.get(4))))
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            frame = ImageProcess(frame)
            writeframe(frame,result)
            OutputFrame("Output", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    return(result)
