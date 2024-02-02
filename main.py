import cv2
import numpy as np

videoname = "canvideo.mp4"









#get video from camera
video = cv2.VideoCapture("canvideo.mp4")
while True:
  #get every frame of video
  ret, frame = video.read()
  #breaks ifi the video has ended
  if frame is None:
      break
  #duplicate the frame




  # Turns into grayscale
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


  # Gaussian Blur
  gray = cv2.GaussianBlur(gray, (15, 15), 0)

  # gets all the edges
  maskedimg = cv2.Canny(gray, 5, 30)


  # hough circles
  circles = cv2.HoughCircles(maskedimg, cv2.HOUGH_GRADIENT, 1.2, 9999, param1=110, param2=60, minRadius=0, maxRadius=90)
  # loops through the circles
  if circles is not None:
      circlelist = np.uint16(np.around(circles))
      # generates a circle and center dot for each circle
      for circle in circlelist[0, :]:
          x = circle[0]
          y = circle[1]
          radius = circle[2]
          # draws the circlel
          cv2.circle(frame, (x, y), radius, (0, 255, 20), 5)

          # draw a dot at the center
          cv2.circle(frame, (x, y), 1, (0, 255, 20), 10)

  # shows new image
  cv2.imshow("e", maskedimg)
  cv2.imshow("Edges", gray)
  cv2.imshow("hi", frame)

  #breaks the video if chracter q is pressed
  if cv2.waitKey(15) & 0xFF == ord('q'):
    break
video.release()
cv2.destroyAllWindows()




