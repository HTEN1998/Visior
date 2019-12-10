import RPi.GPIO as gpio
import time as tt


class CameraControl:
    
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(3,gpio.OUT)
        pwm = gpio.PWM(3, 100)
        pwm.start(0)
        
        gpio.setup(2,gpio.OUT)
        pwm2 = gpio.PWM(2, 100)
        pwm2.start(0)
        
        gpio.output(3, True)
        gpio.output(2, True)
        
        print("Horizontal reset ..")
        pwm.ChangeDutyCycle(210/22+2)
        tt.sleep(0.05)
        print("Vertical reset ..")
        pwm2.ChangeDutyCycle(140/16+2)
        tt.sleep(0.05)
        gpio.output(2,False)
        gpio.output(3,False)
        pwm.stop()
        pwm2.stop()
        gpio.cleanup()
    
    
    
        
        


    def SetAngle(self):
        sleep_time = 0.04
        gpio.setmode(gpio.BCM)
        gpio.setup(3,gpio.OUT)
        pwm = gpio.PWM(3, 100)
        
        gpio.setup(2,gpio.OUT)
        pwm2 = gpio.PWM(2, 100)
        
        pwm.start(0)
        pwm2.start(0)
        
        gpio.output(3, True)
        gpio.output(2,True)
        for duty in range(0,24,1):
            print("+ duty cycle")
            pwm.ChangeDutyCycle(duty)
            pwm2.ChangeDutyCycle(duty)
            tt.sleep(sleep_time)
                
        print("Switch ...")
                
        for duty in range(24,-1,-1):
            print("- duty cycle")
            pwm.ChangeDutyCycle(duty)
            pwm2.ChangeDutyCycle(duty)
            tt.sleep(sleep_time)
                    
        gpio.output(3,False)
        gpio.output(2,False)
        pwm.stop()
        pwm2.stop()
        gpio.cleanup()




    def main(self):
        
        self.SetAngle()
        CameraControl()


if __name__ == "__main__":
    CameraControl().main()