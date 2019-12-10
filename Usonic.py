import RPi.GPIO as gpio
from time import sleep,time
trig = 4
echo = 17
gpio.setmode(gpio.BCM)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

gpio.output(trig,gpio.LOW)
print("Sensor reset ")
sleep(2)
i=0
avg=0
while(1):
	
	gpio.output(trig,gpio.HIGH)
	sleep(0.00001)
	gpio.output(trig,gpio.LOW)


	if(gpio.input(echo)==0):
		print("echo - > 0")
		start = time()
		
	elif(gpio.input(echo)==1):
		print(f"echo - > 1 and i = {i}")
		i+=1
		end = time()
		final_time = end - start
		int_dis = round(final_time*17150,2)
		print(f"intermediate distances = {int_dis} cm")
		if(not(i==25)):
			avg+=int_dis
		else:
			print(f"distance = {avg//25} cm")
			avg=0
			break	
	
		

gpio.cleanup()
