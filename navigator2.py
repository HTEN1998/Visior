class auto_traction():
	
	history_stack=["F","F","F","F","F","L","F","F","F","R","F","F","F","F","F","F","R","F","F","R","F","F","F","F","L","F","F","F"]
	required_direction={"left":0,"right":0}

	def come_back(self):
		print("bot rotated 180 degree to move back")
		while(len(self.history_stack)>0):
			move = self.history_stack.pop()
			if move=="F":
				print("move forward")
			elif move=="R":
				print("move left")
			elif move=="L":
				print("move right")
		print("history_stack is empty")

	def large_area_traction(self):		#gps based traction
		# graphopper.py code here
		#retrun direction_from_api
		pass

	def small_area_traction(self,direction_from_api):#sensor based traction
		#self.compass()
		# compass.py code here
		pass
		
	
	def distance_calculator(self,current_location,goal_location):
		distance = abs(goal_location[0]-current_location[0]+goal_location[1]-current_location[1])
		print("distance= ",distance)
		if distance>2.0:
			print("bot is far")
			self.come_back()
		else:
			print("bot is near")
			direction=self.large_area_traction()
			self.small_focus_traction(direction)

if __name__ == "__main__":
	nv=auto_traction()

	cx,cy = map(float,input("Current: x,y-> ").split(" "))
	current_location=[cx,cy]
	gx,gy = map(float,input("Goal: x,y-> ").split(" "))
	goal_location=[gx,gy]

	nv.distance_calculator(current_location,goal_location)

	nv.navigator
