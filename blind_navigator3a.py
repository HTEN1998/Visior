#navigation in infinite world,removed max-extend
#change motion-funtion names

class Simlutation():

	#max_extend=0
	current_row, current_col = 0,0
	goal_node_row,goal_node_col = 0,0
	blocks=set()
	history=[(-1,-1)]

	def backward_motion(self):
		if (self.current_row-1,self.current_col) in self.blocks:
			return -1
		else:
			if(self.current_row-1,self.current_col) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row-1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def forward_motion(self):
		if (self.current_row+1,self.current_col) in self.blocks:
			return -1
		else:
			if(self.current_row+1,self.current_col) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row+1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def right_motion(self):
		if (self.current_row,self.current_col+1) in self.blocks:
			return -1
		else:
			if(self.current_row,self.current_col+1) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col+1-self.goal_node_col)

	def left_motion(self):
		if (self.current_row,self.current_col-1) in self.blocks :
			return -1
		else:
			if(self.current_row,self.current_col-1) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col-1-self.goal_node_col)

	def backtracker(self):
		temp_tuple = self.history.pop()
		self.blocks.add(temp_tuple)
		temp_tuple = self.history.pop()
		self.navigate(temp_tuple[0],temp_tuple[1])

	def navigate(self,start_row,start_col):
		directions=[]
		self.current_row=start_row
		self.current_col=start_col
		print("Now At-> %d %d"%(self.current_row,self.current_col))

		self.history.append((self.current_row,self.current_col))	#appending previous values
		
		if (self.current_row==self.goal_node_row and self.current_col==self.goal_node_col):	#exit point
			return

		block=input("Does Object present 'up, down, right, left' ?")
		if block[0]=='1':
			tup=(self.current_row-1,self.current_col)
			self.blocks.add(tup)
			del tup
		if block[1]=='1':
			tup = (self.current_row+1,self.current_col)
			self.blocks.add(tup)
			del tup
		if block[2]=='1':
			tup = (self.current_row,self.current_col+1)
			self.blocks.add(tup)
			del tup
		if block[3]=='1':
			tup = (self.current_row,self.current_col-1)
			self.blocks.add(tup)
			del tup

		directions.append(self.backward_motion())
		directions.append(self.forward_motion())
		directions.append(self.right_motion())
		directions.append(self.left_motion())
		print("direction nav-> ",directions)
		min_index=self.get_min_distance(directions)

		if (min_index==0):#up
			self.current_row-=1
			self.navigate(self.current_row,self.current_col)

		elif (min_index==1):#down
			self.current_row+=1
			self.navigate(self.current_row,self.current_col)

		elif (min_index==2):#right
			self.current_col+=1
			self.navigate(self.current_row,self.current_col)

		elif (min_index==3):#left
			self.current_col-=1
			self.navigate(self.current_row,self.current_col)

		elif (min_index==-1):#no direction found
			self.backtracker()

	def setup_world(self):
		#self.max_extend=int(input('Enter matrix size? '))
		self.current_row,self.current_col=map(int,input("Starting Rows Col-> ").split(" "))
		self.goal_node_row,self.goal_node_col=map(int,input("Goal Rows Col-> ").split(" "))

	def get_min_distance(self,directions):
		min,min_index=1000000,-1

		for i in range(len(directions)):
			if directions[i]<min and directions[i]!=-1:
				min=directions[i]
				min_index=i
		return min_index



s=Simlutation()
s.setup_world()
s.navigate(s.current_row,s.current_col)
print("----END----")
print("Path",s.history)
print("blocks",s.blocks)
