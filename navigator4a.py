# inserting gps based stopping condition
import random

class traction_code():

	goal_latitude=0.0
	goal_longitude=0.0
	sensor_data=[-1,-1,-1]

	def   turn_left(self):
		print("Left")

	def   turn_right(self):
		print("Right")

	def move_forward(self):
		print("Forward")

	def direction_decider(self,left_sensor,front_sensor,right_sensor):
		print("3 info direction decider called")
		# print("move  forward to take co-ordinates")
		# self.move_forward()
		# min_distance=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# selected_direction="forward"
		# print("Reverse")
		
		# print("move  left to take co-ordinates")
		# self.  turn_left()
		# temp=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# print("Reverse")
		# if min_distance>temp: 
		# 	min_distance=temp
		# 	selected_direction="left"
		
		# print("move  right to take co-ordinates")
		# self.  turn_right()
		# temp=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# 		print("Reverse")
		# 		if min_distance>temp: 
		# 			min_distance=temp
		# 			selected_direction="right"
		# print("selected_direction= ",selected_direction)
		# return selected_direction

	def direction_decider(self,left_sensor,right_sensor):
		print("2 info direction decider called")		
		# print("move  left to take co-ordinates")
		# self.  turn_left()
		# temp=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# print("Reverse")
		# if min_distance>temp: 
		# 	min_distance=temp
		# 	selected_direction="left"
				
		# print("move  right to take co-ordinates")
		# self.  turn_right()
		# temp=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# 		print("Reverse")
		# 		if min_distance>temp: 
		# 			min_distance=temp
		# 			selected_direction="right"
		# print("selected_direction= ",selected_direction)
		# return selected_direction
	
	def junction_detector(self):
		print("juntion detected, current gps co-ordinates")
		# selected_direction = self.direction_decider(left_sensor,front_sensor,right_sensor)
		# if (selected_direction=="forward"):
		# 	self.move_forward()
		# 	self.navigator()
		# elif (selected_direction=="left"):
		# 	self.turn_left()
		# 	self.navigator()
		# elif (selected_direction=="right"):
		# 	self.turn_right()
		# 	self.navigator()
		i = random.choice([0,1,2])
		if (i==0):
			self.turn_left()
			self.navigator()
		elif (i==1):
			self.move_forward()
			self.navigator()
		elif (i==2):
			self.turn_right()
			self.navigator()
		
	def backtracker(self):
		print("Reverse")
		self.sensor_data[0] = int(input("Left ? "))
		self.sensor_data[2] = int(input("Right ? "))
		# selected_direction = self.direction_decider(left_sensor,right_sensor)
		# if (selected_direction=="left"):
		# 	self.turn_left()
		# 	self.navigator()
		# elif (selected_direction=="right"):
		# 	self.turn_right()
		# 	self.navigator()
		i = random.choice([0,2])
		if (i==0):
			self.  turn_left()
			self.navigator()
		elif (i==2):
			self.  turn_right()
			self.navigator()
		else:
			self.backtracker()


	def navigator(self):
		print("navigation called")

		while (True):
			self.sensor_data[0]=int(input("Left ? "))
			self.sensor_data[1]=int(input("Front ? "))
			self.sensor_data[2]=int(input("Right ? "))
			
			if (self.sensor_data[0]+self.sensor_data[1]+self.sensor_data[2]<=1):	#more than 1 path is available
				self.junction_detector()

			elif(self.sensor_data[0]+self.sensor_data[1]+self.sensor_data[2]>=3):	#no path is available
				print("Dead End")
				self.backtracker()

			else:
				if self.sensor_data[0]==0:
					self.turn_left()
				elif self.sensor_data[1]==0:
					self.move_forward()
				elif self.sensor_data[2]==0:
					self.turn_right()

			if input("stop ? (y/n)")=='y':
				exit()



		
if  __name__ == "__main__":
	t = traction_code()
	print("directions--> [ Left 		Forward 		Right ] ")
	print("for sensor-> 1: block 	0: no block ")
	t.navigator()