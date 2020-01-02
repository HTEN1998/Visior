# navigation by distance calulation
class Simlutation():

	max_extend=0
	current_row, current_col = 0,0
	goal_node_row,goal_node_col = 0,0
	history_row=[-1]
	history_col=[-1]

	def check_up(self,block_row,block_col):
		if(self.current_row-1<0 or (block_row==self.current_row-1 and block_col==self.current_col)):			
			return -1
		else:
			if (self.current_row-1==self.history_row[len(self.history_row)-1] and self.current_col==self.history_col[len(self.history_col)-1]):
				return -1
			return abs(self.current_row-1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def check_down(self,block_row,block_col):
		if(self.current_row+1>self.max_extend or (block_row==self.current_row+1 and block_col==self.current_col)):
			return -1
		else:
			if (self.current_row+1==self.history_row[len(self.history_row)-1] and self.current_col==self.history_col[len(self.history_col)-1]):
				return -1
			return abs(self.current_row+1-self.goal_node_row)+abs(self.current_col-self.goal_node_col)

	def check_right(self,block_row,block_col):
		if(self.current_col+1>self.max_extend or (block_row==self.current_row and block_col==self.current_col+1)):
			return -1
		else:
			if (self.current_row==self.history_row[len(self.history_row)-1] and self.current_col+1==self.history_col[len(self.history_col)-1]):
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col+1-self.goal_node_col)

	def check_left(self,block_row,block_col):
		if(self.current_col-1<0 or (block_row==self.current_row and block_col==self.current_col-1)):
			return -1
		else:
			if (self.current_row==self.history_row[len(self.history_row)-1] and self.current_col-1==self.history_col[len(self.history_col)-1]):
				return -1
			return abs(self.current_row-self.goal_node_row)+abs(self.current_col-1-self.goal_node_col)

	def navigate(self,start_row,start_col):
		directions=[]
		self.current_row=start_row
		self.current_col=start_col
		print("-> %d %d"%(self.current_row,self.current_col))

		block=int(input("?"))
		if block==0:
			block_row, block_col = -1,-1 # no block added 
		elif block==1:
			block_row, block_col = map(int,input("row col-> ").split(" "))

		directions.append(self.check_up(block_row,block_col))
		directions.append(self.check_down(block_row,block_col))
		directions.append(self.check_right(block_row,block_col))
		directions.append(self.check_left(block_row,block_col))
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


	def setup_world(self,sizeof_world):
		self.max_extend=sizeof_world
		self.goal_node_row,self.goal_node_col=map(int,input("Goal Rows Col-> ").split(" "))
		
	def get_decision(self,new_row,new_col):
		
		self.history_row.append(self.current_row)#appending prev location to history
		self.history_col.append(self.current_col)

		self.current_row=new_row
		self.current_col=new_col

		if (self.current_row==self.goal_node_row and self.current_col==self.goal_node_col):
			return

		self.navigate(self.current_row,self.current_col)

	def get_min_distance(self,directions):
		min,min_index=1000000,0

		for i in range(len(directions)):
			if directions[i]<min and directions[i]!=-1:
				min=directions[i]
				min_index=i
		return min_index



s=Simlutation()
s.setup_world(5)
s.navigate(s.current_row,s.current_col)
print('history row-> ',s.history_row)
print('history col-> ',s.history_col)