import RPi.GPIO as gpio
from time import sleep


try:
        gpio.setmode(gpio.BCM)
        gpio.setup(2,gpio.OUT)
        gpio.setup(3,gpio.OUT)
        
        gpio.setup(4,gpio.OUT)
        gpio.setup(17,gpio.OUT)
        
        gpio.setup(27,gpio.OUT)
        gpio.setup(22,gpio.OUT)
        
        gpio.setup(10,gpio.OUT)
        gpio.setup(9,gpio.OUT)

        gpio.output(2,gpio.HIGH)
        gpio.output(3,gpio.LOW)
        gpio.output(4,gpio.HIGH)
        gpio.output(17,gpio.LOW)
        gpio.output(27,gpio.HIGH)
        gpio.output(22,gpio.LOW)
        gpio.output(10,gpio.HIGH)
        gpio.output(9,gpio.LOW)
        print("working...")
        sleep(60)
        print("End")
        gpio.output(2,gpio.LOW)
        gpio.output(3,gpio.LOW)
        gpio.output(4,gpio.LOW)
        gpio.output(17,gpio.LOW)
        gpio.output(27,gpio.LOW)
        gpio.output(22,gpio.LOW)
        gpio.output(10,gpio.LOW)
        gpio.output(9,gpio.LOW)
	
        gpio.cleanup()

except:
	gpio.cleanup()
