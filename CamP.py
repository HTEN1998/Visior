from picamera.array import PiRGBArray as rgbcam
from picamera import PiCamera as cam
from time import sleep

camera = cam()

camera.resolution = (720 , 480)

camera.framerate = 32

camera.start_preview()

camera.start_recording("/home/pi/Desktop/VideoTest.h264")

sleep(10)

camera.stop_recording()

camera.stop_preview()