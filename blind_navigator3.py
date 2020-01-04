#navigation by with backtracking

class Simlutation():

	max_extend=0
	current_row, current_col = 0,0
	goal_node_row,goal_node_col = 0,0
	blocks=set()
	history=[(-1,-1)]

	def check_up(self):
		if(self.current_row-1<0 or (self.current_row-1,self.current_col) in self.blocks):
			return -1
		else:
			if(self.current_row-1,self.current_col) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row-1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def check_down(self):
		if(self.current_row+1>self.max_extend or (self.current_row+1,self.current_col) in self.blocks):
			return -1
		else:
			if(self.current_row+1,self.current_col) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row+1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def check_right(self):
		if(self.current_col+1>self.max_extend or (self.current_row,self.current_col+1) in self.blocks):
			return -1
		else:
			if(self.current_row,self.current_col+1) == self.history[len(self.history)-2]:
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col+1-self.goal_node_col)

	def check_left(self):
		if(self.current_col-1<0 or (self.current_row,self.current_col-1) in self.blocks):
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
		
		if (self.current_row==self.goal_node_row and self.current_col==self.goal_node_col):
			return

		block=int(input("Does Object present [0/1]?"))
		if block==1:
			block_row, block_col = map(int,input("Mention: row col-> ").split(" "))
			tup = (block_row,block_col)
			self.blocks.add(tup)
			del tup

		directions.append(self.check_up())
		directions.append(self.check_down())
		directions.append(self.check_right())
		directions.append(self.check_left())
		print("direction nav-> ",directions)
		min_index=self.get_min_distance(directions)

		if (min_index==0):#up
			self.get_decision(self.current_row-1,self.current_col)
		elif (min_index==1):#down
			self.get_decision(self.current_row+1,self.current_col)
		elif (min_index==2):#right
			self.get_decision(self.current_row,self.current_col+1)
		elif (min_index==3):#left
			self.get_decision(self.current_row,self.current_col-1)
		elif (min_index==-1):#no direction found
			self.backtracker()

	def setup_world(self):
		self.max_extend=int(input('Enter matrix size? '))
		self.goal_node_row,self.goal_node_col=map(int,input("Goal Rows Col-> ").split(" "))

	def get_decision(self,new_row,new_col):

		# self.history.append((self.current_row,self.current_col))	#appending previous values
		
		self.current_row=new_row
		self.current_col=new_col

		self.navigate(self.current_row,self.current_col)

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