from random import randrange
class Simlutation():

	world=[["T","B","P","B"],
		["S","n","B","n"],
		["W","SBG","P","B"],
		["S","n","B","n"]]	
			
	memory=[["n","n","n","n"],
			["n","n","n","n"],
			["n","n","n","n"],
			["n","n","n","n"]]

	# history_row=[]
	# history_col=[]

	current_row, current_col = 0,0

	def check_up(self,also_check):
		if(self.current_row-1<0 or self.memory[self.current_row-1][self.current_col]==also_check):
			return 0
		else: return 1
	def check_down(self,also_check):
		if(self.current_row+1>3 or self.memory[self.current_row+1][self.current_col]==also_check):
			return 0
		else: return 1
	def check_right(self,also_check):
		if(self.current_col+1>3 or self.memory[self.current_row][self.current_col+1]==also_check):
			return 0
		else: return 1
	def check_left(self,also_check):
		if(self.current_col-1<0 ):
			return 0
		else: return 1
	
	def place_senses(self,row,col,sense_name):
			
			available_directions=[]
			available_directions.append(self.check_up('v'))
			available_directions.append(self.check_down('v'))
			available_directions.append(self.check_right('v'))
			available_directions.append(self.check_left('v'))
			print("place_senses",available_directions)

			if (available_directions[0]==1):#up 
				if(self.memory[row-1][col]!='v'):
					if(self.memory[row-1][col]=='n'):
						self.memory[row-1][col]=sense_name
					else:
						self.memory[row-1][col]+=sense_name

			if (available_directions[1]==1):#down
				if(self.memory[row+1][col]!='v'):
					if(self.memory[row+1][col]=='n'):
						self.memory[row+1][col]=sense_name
					else:
						self.memory[row+1][col]+=sense_name

			if (available_directions[2]==1):#right
				if(self.memory[row][col+1]!='v'):
					if(self.memory[row][col+1]=='n'):
						self.memory[row][col+1]=sense_name
					else:
						self.memory[row+1][col]+=sense_name

			if (available_directions[3]==1):#left
				if(self.memory[row][col-1]!='v'):
					if(self.memory[row][col-1]=='n'):
						self.memory[row][col-1]=sense_name
					else:
						self.memory[row][col-1]+=sense_name
		
			


	def place_blockages(self,blockage_name):

		sense_name=""
		if blockage_name=='W':
			sense_name='S'
		elif blockage_name=='P':
			sense_name='B'

		available_directions=[]
		available_directions.append(self.check_up('v'))
		available_directions.append(self.check_down('v'))
		available_directions.append(self.check_right('v'))
		available_directions.append(self.check_left('v'))
		
		print("place_blockages",available_directions)

		if (available_directions[0]==1):#up  check for visted location before adding block name
			#if(self.memory[self.current_row-1][self.current_col]!='v'):				
			self.memory[self.current_row-1][self.current_col]=blockage_name
			self.place_senses(self.current_row-1,self.current_col,sense_name)

		if (available_directions[1]==1):#down
			#if(self.memory[self.current_row+1][self.current_col]!='v'):
			self.memory[self.current_row+1][self.current_col]=blockage_name
			self.place_senses(self.current_row+1,self.current_col,sense_name)

		if (available_directions[2]==1):#right
			#if(self.memory[self.current_row][self.current_col+1]!='v'):
			self.memory[self.current_row][self.current_col+1]=blockage_name
			self.place_senses(self.current_row,self.current_col+1,sense_name)

		if (available_directions[3]==1):#left
			#print("left")
			#if(self.memory[self.current_row][self.current_col-1]!='v'):
			self.memory[self.current_row][self.current_col-1]=blockage_name
			self.place_senses(self.current_row,self.current_col-1,sense_name)

	def navigate(self,start_row,start_col):
		directions=[]
		self.current_col=start_col
		self.current_row=start_row
		self.memory[self.current_row][self.current_col]='v'

		#check for stench/breeze in current position
		if(self.world[self.current_row][self.current_col]=='S' or self.world[self.current_row][self.current_col]=='B'):
			print("senses present")
			if(self.world[self.current_row][self.current_col]=='S'):
				self.place_blockages('W')
			elif(self.world[self.current_row][self.current_col]=='B'):
				self.place_blockages('P')

			return self.current_row,self.current_col
		else:
			print("senses absent")
			directions.append(self.check_up('v'))
			directions.append(self.check_down('v'))
			directions.append(self.check_right('v'))
			directions.append(self.check_left('v'))
			print("direction -> ",directions)
			if (directions[0]==1):#up
				return self.current_row-1,self.current_col
			elif (directions[1]==1):#down
				return self.current_row+1,self.current_col
			elif (directions[2]==1):#right
				return self.current_row,self.current_col+1
			elif (directions[3]==1):#left
				return self.current_row,self.current_col-1				



def print_matrix(m):
	print("-------------------------------")
	for i in range(4):
		for j in range(4):
			print(m[i][j],end=" ")
		print()


s=Simlutation()
row, col = s.navigate(0,0)		#1st move
print(row)
print(col)
# s.history_row.append(row)
# s.history_col.append(col)
print_matrix(s.memory)

row, col = s.navigate(row,col)		#2nd move
print(row)
print(col)
print_matrix(s.memory)

row, col = s.navigate(0,0)		#3rd move
print(row)
print(col)
print_matrix(s.memory)

row, col = s.navigate(row,col)		#4th move
print(row)
print(col)
print_matrix(s.memory)
