from FrameProcessing import *
from FrameOutput import *
def VideoProcessing(video):
    while True:
        ret, frame = video.read()
        if not ret:
            break
        else:
            frame = ImageProcess(frame)
            OutputFrame("Output", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
