import RPi.GPIO as io


io.setmode(io.BCM)
io.setup(4,io.OUT)


print("Started ...")
i=0
while(i<=50000):
	print(f"Executed -> {i}")
	i+=1	

	io.output(4,io.HIGH)
io.cleanup()
