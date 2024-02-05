from CaptureVideo import *
from VideoProcess import *
from VideoReleasing import *

videoname = "canvideo.mp4"


video = CaptureVid(videoname)
result = VideoProcessing(video)
ReleaseVideo(video)
ReleaseVideo(result)
destroy()
