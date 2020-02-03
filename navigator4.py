import random

class traction_code():

	goal_latitude=0.0
	goal_longitude=0.0

	def turn_left(self):
		print("Left")

	def turn_right(self):
		print("Right")

	def move_forward(self):
		print("Forward")
	
	def junction_detector(self):
		print("juntion detected, current gps co-ordinates")
		
		# print("move  forward to take co-ordinates")
		# self.move_forward()
		# min_distance=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# selected_direction="forward"
		# print("Reverse")
		
		# print("move  left to take co-ordinates")
		# self.turn_left()
		# temp=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# print("Reverse")
		# if min_distance>temp: 
		# 	min_distance=temp
		# 	selected_direction="left"
		
		# print("move  right to take co-ordinates")
		# self.turn_right()
		# temp=(goal_latitude-current_latitude)+(goal_longitude-current_longtitude)
		# 		print("Reverse")
		# 		if min_distance>temp: 
		# 			min_distance=temp
		# 			selected_direction="right"
		# print("selected_direction= ",selected_direction)
		
		print("suppose shortest direction is Forward")	
		self.move_forward()
		self.navigator()
		
	def backtracker(self):
		print("Reverse")
		left_sensor=int(input("Left ? "))
		right_sensor=int(input("Right ? "))
		if (left_sensor==0):
			self.turn_left()
			self.navigator()
		elif (right_sensor==0):
			self.turn_right()
			self.navigator()
		elif(left_sensor==1 and right_sensor==1):
			self.backtracker()


	def navigator(self):
		print("navigation called")

		while (True):
			left_sensor=int(input("Left ? "))
			front_sensor=int(input("Front ? "))
			right_sensor=int(input("Right ? "))
			
			if (left_sensor+right_sensor+front_sensor<=1):
				self.junction_detector()

			elif(left_sensor+right_sensor+front_sensor>=3):
				print("Dead End")
				self.backtracker()

			else:
				if left_sensor==0:
					self.turn_left()
				elif front_sensor==0:
					self.move_forward()
				elif right_sensor==0:
					self.turn_right()

			if input("stop ? (y/n)")=='y':
				exit()
				# print("traction stoppped !")
				# break



		
if  __name__ == "__main__":
	t = traction_code()
	print("directions--> [ Left 		Forward 		Right ] ")
	print("for sensor-> 1: block 	0: no block ")
	t.navigator()