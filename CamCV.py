import cv2 as cv
from picamera.array import PiRGBArray as rgbcam
from picamera import PiCamera as cam
from time import sleep
import matplotlib.pyplot as plt


camera = cam()
rawPic = rgbcam(camera)

sleep(0.1)

camera.capture(rawPic,format="bgr")
image = rawPic.array

plt.imshow(image)
plt.show()
#cv.imshow("Image",image)

