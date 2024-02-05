from CaptureVideo import *
from VideoProcess import *
from VideoReleasing import *

videoname = "canvideo.mp4"

#captures video
video = CaptureVid(videoname)
#processes video and outputs
result = VideoProcessing(video)
#releases video
ReleaseVideo(video)
ReleaseVideo(result)
destroy()
