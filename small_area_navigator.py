from UltrasonicDriver import UltraSonicControl
from MotorDriver import *

class auto_traction():

	compass_angle=0
	front_sensor=0
	left_sensor=0
	right_sensor=0

	def go_forward(self):
		count=0
		b = UltraSonicControl()
		while(count<10):
				front_tuple = b.CheckFront()
				self.front_sensor = int(front_tuple[0])
				# self.front_sensor=int(input("forward block? "))	#asking front sensor
				if self.front_sensor==1:
					return				
				else:
					print("go_forward: ----->  move forward")	#drive bot to front
					MoveForward()
					count+=1

	def reset_compass_angle(self,angle):
		if angle==360 or angle==-360:
			angle=0
		print("reset_compass_angle: called angle= ",angle)
		return angle

	def backtracker(self):
		print("backtracker: called")
		b = UltraSonicControl()
		while(True):
			print("backtracker: ----->  move back")
			MoveBackward()

			# self.left_sensor=int(input("backtracker: left block? "))
			left_tuple = b.CheckLeft()
			self.left_sensor = int(left_tuple[0])
			# self.right_sensor=int(input("backtracker: right block? "))
			right_tuple = b.CheckRight()
			self.right_sensor = int(right_tuple[0])
			if(self.left_sensor==0):
				self.compass_angle+=90
				self.compass_angle = self.reset_compass_angle(self.compass_angle)
				print("backtracker: ----->  turn left")	
				MoveLeft()
				return
			elif(self.right_sensor==0):
				self.compass_angle-=90
				self.compass_angle = self.reset_compass_angle(self.compass_angle)
				print("backtracker: ----->  turn right")	
				MoveRight()
				return

	def compass(self,input_direction):
		print("compass: called")
		count = 0
		b = UltraSonicControl()
		if input_direction=="left":
			print("compass: intial  turn left")
			MoveLeft()
			self.go_forward()
		elif input_direction=="right":
			print("compass : intial turn right")
			MoveRight()
			self.go_forward()
		elif input_direction=="front":
			print("compass : intial front motion")
			self.go_forward()

		while (count<2):
			print("compass: loop started",count)

			# self.left_sensor=int(input("Compass: left block? "))
			left_tuple = b.CheckLeft()
			self.left_sensor = int(left_tuple[0])
			# self.right_sensor=int(input("Compass: right block? "))
			right_tuple = b.CheckRight()
			self.right_sensor = int(right_tuple[0])
			if(self.left_sensor==0 and self.right_sensor==0):	#no block detected in left and right
				
				temp_left_angle=self.compass_angle+90
				temp_right_angle=self.compass_angle-90

				# covert 360 degree to zero
				temp_left_angle = self.reset_compass_angle(temp_left_angle)
				temp_right_angle = self.reset_compass_angle(temp_right_angle)

				left_list=[abs(-360-temp_left_angle),abs(360-temp_left_angle),abs(0-temp_left_angle)]
				right_list=[abs(-360-temp_right_angle),abs(360-temp_right_angle),abs(0-temp_right_angle)]
				
				if (min(left_list)<min(right_list)):	# move left is compass angle is near to 360 or 0 degree
					if(left_tuple[1]>right_tuple[1]):
						print("compass ----->   turn left")
						self.compass_angle+=90
						self.compass_angle = self.reset_compass_angle(self.compass_angle)
						MoveLeft()
						self.go_forward()
					else:
						print("compass ----->   turn right")
						self.compass_angle-=90
						self.compass_angle = self.reset_compass_angle(self.compass_angle)
						MoveRight()
						self.go_forward()

				elif(min(left_list)>=min(right_list)):
					if(left_tuple[1]<right_tuple[1]):
						print("compass -----> turn right")
						self.compass_angle-=90
						self.compass_angle = self.reset_compass_angle(self.compass_angle)
						MoveRight()
						self.go_forward()
					else:
						print("compass -----> turn left")
						self.compass_angle+=90
						self.compass_angle = self.reset_compass_angle(self.compass_angle)
						MoveLeft()
						self.go_forward()

			elif(self.left_sensor==0 and self.right_sensor==1): #no block detected on left 
					print("compass -----> turn left")
					self.compass_angle+=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					MoveLeft()
					self.go_forward()

			elif(self.left_sensor==1 and self.right_sensor==0): #no block detected on right 
					print("compass -----> turn right")
					self.compass_angle-=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					MoveRight()
					self.go_forward()

			elif(self.left_sensor==1 and self.right_sensor==1):  #dead end conditon
				# self.front_sensor=int(input("compass: forward block? "))	#checking front sensor to finalize dead end
				front_tuple = b.CheckFront()
				self.front_sensor = int(front_tuple[0])
				if self.front_sensor==1:
					self.backtracker()
				else:
					self.go_forward()
			count+=1
			
					
nv=auto_traction()
print("gps command: move forward direction")
nv.compass("front")
print("waiting for next command from gps")
# nv.compass("left")
# nv.compass("right")