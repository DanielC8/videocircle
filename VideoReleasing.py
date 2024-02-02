import cv2

#releases the video and destroys all windows

def ReleaseVideo(video):
    video.release()
    cv2.destroyAllWindows()