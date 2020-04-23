# from UltrasonicDriver import UltraSonicControl
# from MotorDriver import *
# from time import sleep

class auto_traction():

	compass_angle=0
	front_sensor=False
	left_sensor = False
	right_sensor = False
	b=""

	# def __init__(self):
	# 	self.b = UltraSonicControl()
	# 	InitilaizePins()
	# 	print("Pins Initilaized : Ultrasonic Up")

	def go_forward(self):
		b = self.b
		while True:
				self.front_sensor = input("front block detected ? ").title() == "True"
				# self.front_sensor = b.CheckFront()[0]		#asking front sensor
				if self.front_sensor == True:
					# MoveBackward()
					# sleep(0.1)
					# ResetMotorPins()
					return				
				elif self.front_sensor == False:
					print("angle:{} compass: {}".format(self.compass_angle,"move forward"))	#drive bot to front
					# MoveForward()

	def reset_compass_angle(self,angle):
		if angle==360 or angle==-360:
			angle=0
		# print("reset_compass_angle: angle= ",angle)
		return angle

	def backtracker(self):
		# b = self.b
		print("backtracker: called")
		while(True):
			print("backtracker: --------------->  move back")
			#MoveBackward()
			# sleep(0.5)
			# MoveForward()
			# sleep(0.1)
			# ResetMotorPins()

			self.left_sensor = input("left block detected? ").title() == "True"
			self.right_sensor = input("rightblock detected ? ").title() == "True"
			# self.left_sensor=b.CheckLeft()[0]
			# sleep(1)
			# self.right_sensor=b.CheckRight()[0]
			# sleep(1)
			
			if(self.left_sensor==False):
				self.compass_angle+=90
				self.compass_angle = self.reset_compass_angle(self.compass_angle)
				print("angle:{} backtracker: {}".format(self.compass_angle,"move left"))
				#MoveLeft()
				# sleep(0.5)
				return
			elif(self.right_sensor==False):
				self.compass_angle-=90
				self.compass_angle = self.reset_compass_angle(self.compass_angle)
				print("angle:{} compass: {}".format(self.compass_angle,"move right"))
				#MoveRight()
				# sleep(0.5)
				return


	def compass(self,input_direction):
		print("compass: called")
		# b = self.b
		if input_direction=="stop":
			print("compass : stopped")
			return
		elif input_direction=="left":
			print("compass: intial  turn left")
			# MoveLeft()
			# go_forward()
		elif input_direction=="right":
			print("compass : intial turn right")
			# MoveRight()
			# self.go_forward()
		elif input_direction=="front":
			print("compass : intial front motion")
			self.go_forward()

		while True:

			self.left_sensor = input("left clear ? ").title() == "True"
			self.right_sensor = input("right clear ? ").title() == "True"
			# self.left_sensor = b.CheckLeft()[0]
			# sleep(1)
			# self.right_sensor = b.CheckRight()[0]
			# sleep(1)
			if(self.left_sensor==False and self.right_sensor==False):	#no block detected in left and right
				temp_left_angle=self.compass_angle+90
				temp_right_angle=self.compass_angle-90

				# covert 360 degree to zero
				temp_left_angle = self.reset_compass_angle(temp_left_angle)
				temp_right_angle = self.reset_compass_angle(temp_right_angle)

				left_list=[abs(-360-temp_left_angle),abs(360-temp_left_angle),abs(0-temp_left_angle)]
				right_list=[abs(-360-temp_right_angle),abs(360-temp_right_angle),abs(0-temp_right_angle)]
				if (min(left_list)<min(right_list)):	# move left is compass angle is near to 360 or 0 degree
					self.compass_angle+=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					print("angle:{} compass: {}".format(self.compass_angle,"move left"))
					# MoveLeft()

				elif(min(left_list)>=min(right_list)):
					self.compass_angle-=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					print("angle:{} compass: {}".format(self.compass_angle,"move right"))
					# MoveRight()


			elif(self.left_sensor==False and self.right_sensor==True): #no block detected on left 
					self.compass_angle+=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					print("angle:{} compass: {}".format(self.compass_angle,"move left"))
					# MoveLeft()

			elif(self.left_sensor==True and self.right_sensor==False): #no block detected on right 
					self.compass_angle-=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					print("angle:{} compass: {}".format(self.compass_angle,"move right"))
					# MoveRight()

			elif(self.left_sensor==True and self.right_sensor==True):  #dead end conditon
				self.backtracker()
			self.go_forward()
			
					
nv=auto_traction()
print("gps command: move forward direction")
nv.compass("front")
print("waiting for next command from gps")
# nv.compass("left")
# nv.compass("right")
