import requests

class auto_traction():
	
	def come_back(self):
		pass

	def large_area_traction(self,cx,cy,gx,gy):		#gps based traction
		r = requests.get("https://graphhopper.com/api/1/route?point="+str(cx)+","+str(cy)+"&point="+str(gx)+","+str(gy)+"&vehicle=foot&locale=en&calc_points=true&key=apikey")
		# pprint(r.json())
		data = r.json()
		direction = []
		length = len(data['paths'][0]['instructions'])
		print("length= ",length)
		for i in range(0,length):
			direction.append(data['paths'][0]['instructions'][i]['sign'])
		# small_area_traction(direction[0])
		return direction[0]
		

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
	nv.large_area_traction(cx,cy,gx,gy)
