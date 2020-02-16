class auto_traction():
	
	history_stack=["F","F","F","F","F","L","F","F","F","R","F","F","F","F","F","F","R","F","F","R","F","F","F","F","L","F","F","F"]
	required_direction={"left":0,"right":0}

	def go_forward():
	front_sensor="no block"
	while(front_sensor!="block"):
			print("------------>  move forward")	#drive bot to front
			front_sensor=input("forward block? ")	#asking front sensor

	def compass(self):
		if(input_direction=="forward"):
			go_forward()

			left_sensor=input("left block? ")	#asking left sensor
			right_sensor=input("right block? ")	#asking right sensor
			if(left_sensor=='0' and right_sensor=='0'):
				if(required_direction["left"]>required_direction["right"]):
					print("------------>  turn left")
					required_direction["left"]+=1
					if(required_direction["right"]>0):required_direction["right"]-=1
					go_forward()
				elif(required_direction["left"]<required_direction["right"]):
					print("------------>  turn right")
					required_direction["right"]+=1
					if(required_direction["left"]>0):required_direction["left"]-=1
					go_forward()
				else:
					print("------------>  turn left")#default turn
					required_direction["right"]+=1				
			elif(left_sensor=='0' and right_sensor=='1'):
				print("------------>  turn left")
				required_direction["right"]+=1
				if(required_direction["leftt"]>0):required_direction["leftt"]-=1
				go_forward()
			elif(left_sensor=='1' and right_sensor=='0'):
				print("------------>  turn right")
				required_direction["left"]+=1
				if(required_direction["right"]>0):required_direction["right"]-=1
				go_forward()
			elif(left_sensor=='1' and right_sensor=='1'):
				print("------------>  move backward")

		elif(input_direction=="left"):
			pass
		elif(input_direction=="right"):
			pass

		print(required_direction)
		compass(input_direction)

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

	def long_focus_traction(self):#gps based traction
		#retrun direction_from_api
		pass

	def small_focus_traction(self,direction_from_api):#sensor based traction
		#self.compass()
		pass
		
	
	def distance_calculator(self,current_location,goal_location):
		distance = abs(goal_location[0]-current_location[0]+goal_location[1]-current_location[1])
		print("distance= ",distance)
		if distance>2.0:
			print("bot is far")
			self.come_back()
		else:
			print("bot is near")
			direction=self.long_focus_traction()
			self.small_focus_traction(direction)

if __name__ == "__main__":
	nv=auto_traction()

	cx,cy = map(float,input("Current: x,y-> ").split(" "))
	current_location=[cx,cy]
	gx,gy = map(float,input("Goal: x,y-> ").split(" "))
	goal_location=[gx,gy]

	nv.distance_calculator(current_location,goal_location)

	nv.navigator