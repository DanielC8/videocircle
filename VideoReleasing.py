import cv2

#releases the video and destroys all windows

def ReleaseVideo(video):
    video.release()
def destroy():
    cv2.destroyAllWindows()
