# from UltrasonicDriver import UltraSonicControl
# from MotorDriver import *
import time

class auto_traction():

	compass_angle=0
	front_sensor=0
	left_sensor=0
	right_sensor=0

	def go_forward(self):
		count=0
		# b = UltraSonicControl()
		while(count<10):
				self.front_sensor=int(input("forward block? "))	#asking front sensor
				# b.UltrasonicLookInFront()
				# self.front_sensor = int(not b.clearAhead(True))
				if self.front_sensor==1:
					return
				else:
					print("------------>  move forward")	#drive bot to front
					# MoveForward()
					count+=1

	def reset_compass_angle(self,angle):
		if angle==360 or angle==-360:
			angle=0
		return angle

	def backtracker(self):
		#b = UltraSonicControl()
		while(True):
			print("------------>  move back")
			#MoveBackward()

			self.left_sensor=int(input("backtracker: left block? "))
			# b.UltrasonicLookLeft(0)
			# self.left_sensor = int(not b.clearAhead(True))
			self.right_sensor=int(input("backtracker: right block? "))
			# b.UltrasonicLookRight(180)
			# self.right_sensor = int(not b.clearAhead(True))
			if(self.left_sensor==0):
				self.compass_angle+=90
				self.compass_angle = self.reset_compass_angle(self.compass_angle)
				print("------------>  turn backtracker left")	
				#MoveLeft()
				return
			elif(self.right_sensor==0):
				self.compass_angle-=90
				self.compass_angle = self.reset_compass_angle(self.compass_angle)
				print("------------>  turn backtracker right")	
				#MoveRight()
				return


	def compass(self,input_direction):
		count = 0
		#timeout = time.time()+10		#loop runs for 10 seconds
		#b = UltraSonicControl()
		while (count<10):

			if input_direction=="left":
				print("------------>  turn left")
				# MoveLeft()
				# go_forward()
			elif input_direction=="right":
				print("------------>  turn right")
				# MoveRight()
				# self.go_forward()
			elif input_direction=="front":
				self.go_forward()

			self.left_sensor=int(input("Compass: left block? "))
			# b.UltrasonicLookLeft(0)
			# self.left_sensor = int(not b.clearAhead(True))
			self.right_sensor=int(input("Compass: right block? "))
			# b.UltrasonicLookRight(180)
			# self.right_sensor = int(not b.clearAhead(True))
			if(self.left_sensor==0 and self.right_sensor==0):	#no block detected in left and right
				temp_left_angle=self.compass_angle+90
				temp_right_angle=self.compass_angle-90

				# covert 360 degree to zero
				temp_left_angle = self.reset_compass_angle(temp_left_angle)
				temp_right_angle = self.reset_compass_angle(temp_right_angle)

				left_list=[abs(-360-temp_left_angle),abs(360-temp_left_angle),abs(0-temp_left_angle)]
				right_list=[abs(-360-temp_right_angle),abs(360-temp_right_angle),abs(0-temp_right_angle)]
				
				if (min(left_list)<min(right_list)):	# move left is compass angle is near to 360 or 0 degree
					print("------------> compass  turn left")
					self.compass_angle+=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					# MoveLeft()
					# self.go_forward()

				elif(min(left_list)>=min(right_list)):
					print("------------>  compass turn right")
					self.compass_angle-=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					# MoveRight()
					# self.go_forward()


			elif(self.left_sensor==0 and self.right_sensor==1): #no block detected on left 
					print("------------>  comapss turn left")
					self.compass_angle+=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					# MoveLeft()
					# self.go_forward()

			elif(self.left_sensor==1 and self.right_sensor==0): #no block detected on right 
					print("------------>  compass turn right")
					self.compass_angle-=90
					self.compass_angle = self.reset_compass_angle(self.compass_angle)
					# MoveRight()
					# self.go_forward()

			elif(self.left_sensor==1 and self.right_sensor==1):  #dead end conditon
				self.front_sensor=int(input("forward block? "))	#checking front sensor to finalize dead end
				# b.UltrasonicLookInFront()
				# self.front_sensor = int(not b.clearAhead(True))
				if self.front_sensor==1:
					self.backtracker()
			if count==2:
				print("compass end",count)
				return
		
		
nv=auto_traction()
print("gps command: move forward direction")
nv.compass("front")
print("waiting for next command from gps")
# nv.compass("left")
# nv.compass("right")
