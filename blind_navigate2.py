# navigation by distance calulation

class Simlutation():

	max_extend=0
	current_row, current_col = 0,0
	goal_node_row,goal_node_col = 0,0
	history=[(-1,-1)]

	def check_up(self,block_row,block_col):
		if(self.current_row-1<0 or (block_row==self.current_row-1 and block_col==self.current_col)):
			return -1
		else:
			if (self.current_row-1==self.history[len(self.history)-1][0] and self.current_col==self.history[len(self.history)-1][1]):
				return -1
			return abs(self.current_row-1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def check_down(self,block_row,block_col):
		if(self.current_row+1>self.max_extend or (block_row==self.current_row+1 and block_col==self.current_col)):
			return -1
		else:
			if (self.current_row+1==self.history[len(self.history)-1][0] and self.current_col==self.history[len(self.history)-1][1]):
				return -1
			return abs(self.current_row+1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def check_right(self,block_row,block_col):
		if(self.current_col+1>self.max_extend or (block_row==self.current_row and block_col==self.current_col+1)):
			return -1
		else:
			if (self.current_row==self.history[len(self.history)-1][0] and self.current_col+1==self.history[len(self.history)-1][1]):
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col+1-self.goal_node_col)

	def check_left(self,block_row,block_col):
		if(self.current_col-1<0 or (block_row==self.current_row and block_col==self.current_col-1)):
			return -1
		else:
			if (self.current_row==self.history[len(self.history)-1][0] and self.current_col-1==self.history[len(self.history)-1][1]):
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col-1-self.goal_node_col)

	def navigate(self,start_row,start_col):
		directions=[]
		self.current_row=start_row
		self.current_col=start_col
		print("Now At-> %d %d"%(self.current_row,self.current_col))

		if (self.current_row==self.goal_node_row and self.current_col==self.goal_node_col):
			return

		block=input("Does Object present [y/n]?")
		if block=='n':
			block_row, block_col = -1,-1 # no block added
		elif block=='y':
			block_row, block_col = map(int,input("Mention: row col-> ").split(" "))

		directions.append(self.check_up(block_row,block_col))
		directions.append(self.check_down(block_row,block_col))
		directions.append(self.check_right(block_row,block_col))
		directions.append(self.check_left(block_row,block_col))
		print("direction nav-> ",directions)
		min_index=self.get_min_distance(directions)
		#print("min_index-> ",min_index)

		if (min_index==0):#up
			self.get_decision(self.current_row-1,self.current_col)
		elif (min_index==1):#down
			self.get_decision(self.current_row+1,self.current_col)
		elif (min_index==2):#right
			self.get_decision(self.current_row,self.current_col+1)
		elif (min_index==3):#left
			self.get_decision(self.current_row,self.current_col-1)
		elif (min_index==-1):#no direction found
			x = self.history.pop()
			print("prev_row = %d & prev_col = %d"%(x[0], x[1]))

	def setup_world(self,sizeof_world):
		self.max_extend=sizeof_world
		self.goal_node_row,self.goal_node_col=map(int,input("Goal Rows Col-> ").split(" "))

	def get_decision(self,new_row,new_col):

		self.history.append((self.current_row,self.current_col))	#appending previous values
		
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
s.setup_world(4)
s.navigate(s.current_row,s.current_col)
print("----END----")
print("Path",s.history)
