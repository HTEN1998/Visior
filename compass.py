
class auto_traction():

	compass_angle=0
	front_sensor="no block"
	left_sensor="no block"
	right_sensor="no block"

	def go_forward(self):
		count=0
		while(count<5):
				print("------------>  move forward")	#drive bot to front
				count+=1
				self.front_sensor=input("forward block? ")	#asking front sensor
				if self.front_sensor=="block":break

	def reset_compass_angle(self):
		if self.compass_angle==360 or self.compass_angle==-360:
			self.compass_angle=0

	def compass(self,input_direction):
		
		if input_direction=="left":
			print("------------>  turn left")
			go_forward()
		elif input_direction=="right":
			print("------------>  turn right")
			self.go_forward()
		elif input_direction=="front":
			self.go_forward()

		self.left_sensor=input("left block? ")
		self.right_sensor=input("right block? ")
		if(self.left_sensor=='0' and self.right_sensor=='0'):	#no block detected in left and right
			temp_left_angle=self.compass_angle+90
			temp_right_angle=self.compass_angle-90

			# covert 360 degree to zero
			if(temp_left_angle==360 or temp_left_angle==-360): temp_left_angle=0
			if(temp_right_angle==360 or temp_right_angle==-360): temp_right_angle=0

			left_list=[abs(-360-temp_left_angle),abs(360-temp_left_angle),abs(0-temp_left_angle)]
			right_list=[abs(-360-temp_right_angle),abs(360-temp_right_angle),abs(0-temp_right_angle)]
			if (min(left_list)<min(right_list)):
				print("------------>  turn left")
				self.compass_angle+=90
				self.reset_compass_angle()
				self.go_forward()

			elif(min(left_list)>min(right_list)):
				print("------------>  move right")
				self.compass_angle-=90
				self.reset_compass_angle()
				self.go_forward()
			else:
				print("------------>  move right")
				self.compass_angle-=90
				self.reset_compass_angle()
				self.go_forward()


		elif(self.left_sensor=='0' and self.right_sensor=='1'): #no block detected on left 
				print("------------>  move left")
				self.compass_angle+=90
				self.reset_compass_angle()
				self.go_forward()

		elif(self.left_sensor=='1' and self.right_sensor=='0'): #no block detected on right 
				print("------------>  move right")
				self.compass_angle-=90
				self.reset_compass_angle()
				self.go_forward()

		elif(self.left_sensor=='1' and self.right_sensor=='1'):  #dead end conditon
			print("------------>  move back")
		
		
nv=auto_traction()
for i in range(5):nv.compass("front")
# nv.compass("left")
# nv.compass("right")