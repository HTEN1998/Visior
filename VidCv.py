import cv2
from picamera.array import PiRGBArray as rgbcam
from picamera import PiCamera as cam
from time import sleep
import matplotlib.pyplot as plt


res = (480 , 368)
camera = cam()
camera.resolution = res
camera.framerate = 32
camera.exposure_mode = 'auto'
camera.awb_mode = 'flash'
rawCap = rgbcam(camera , size=res)

sleep(0.1)

for frame in camera.capture_continuous(rawCap,format="bgr" ,use_video_port=True):
    image = frame.array
    cv2.imshow("Video" , image)
    key = cv2.waitKey(1) & 0xFF
    rawCap.truncate(0)
    
    if key == ord("q"):
        break
