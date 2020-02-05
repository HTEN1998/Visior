#navigation with random choice of direction
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
	
	def junction_detector(self):
		print("juntion detected, current gps co-ordinates")
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
		
		if(self.sensor_data[0]+self.sensor_data[2]>=2): #blockage in left and right
			self.backtracker()

		elif(self.sensor_data[0]+self.sensor_data[2]==0):#no blockage in left and right
			i = random.choice([0,2])	
			if (i==0):
				self.turn_left()
				self.navigator()
			elif (i==2):
				self.turn_right()
				self.navigator()

		elif(self.sensor_data[0]==0): #blockage in left
			self.turn_left()
			self.navigator()

		elif(self.sensor_data[2]==0):#blockage in right
			self.turn_right()
			self.navigator()			
				

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
