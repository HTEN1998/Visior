
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
		if input_direction=="front":
			self.go_forward()
			self.left_sensor=input("left block? ")
			self.right_sensor=input("right block? ")
			if(self.left_sensor=='0' and self.right_sensor=='0'):	#no block detected in left and right

			elif(self.left_sensor=='1' and self.right_sensor=='0'): #no block detected on left 
				print("------------>  move left")
				self.compass_angle+=90
				self.reset_compass_angle()
				self.go_forward()

			elif(self.left_sensor=='0' and self.right_sensor=='1'): #no block detected on right 
				print("------------>  move right")
				self.compass_angle-=90
				self.reset_compass_angle()
				self.go_forward()

			elif(self.left_sensor=='1' and self.right_sensor=='1'):  #dead end conditon
				print("------------>  move back")
				

		elif input_direction=="left":
			print("------------>  turn left")
			self.go_forward()
		elif input_direction=="right":
			print("------------>  turn right")
			self.go_forward()

nv=auto_traction()
nv.compass()