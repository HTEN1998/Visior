import string
import time as t
from random import randrange

class a_star:
	graph=[]
	h_value={}
	mapper={}
	distance={}

	def  get_biginput(self,maxnodes,min_cost,max_cost):
		row = []
		self.graph = []
		for i in range(maxnodes):
			for j in range(maxnodes):
				row.append(randrange(min_cost,max_cost))
			self.graph.append(row.copy())
			row.clear()

		count=0
		characters=string.ascii_uppercase[:]
		for i in characters:
			for j in characters:
				count+=1
				self.h_value[i+j]=randrange(0,10)
				self.mapper[i+j]=count
				#print("count",count)
				if(count==maxnodes):return

	def  get_value(self,keystring):
		key=keystring.split(",")
		sum=0
		for i in range(0,len(key)-1):
			sum+=self.graph[self.mapper[key[i]]][self.mapper[key[i+1]]]
		sum+=self.h_value[key[len(key)-1]]
		return sum

	def generate_distance(self,keystring):
		#print("keystring",keystring)
		value=self.get_value(keystring)
		self.distance[keystring]=value

	def check_row(self,label,maxnodes):
		#print(label)
		labelist=label.split(",")
		#print("labelist",labelist)
		rowlabel=labelist[len(labelist)-1]
		for i in range(1,maxnodes):
			#print("rowlabel",rowlabel)
			if (self.graph[self.mapper[rowlabel]][i]!=0):
				self.generate_distance(label+","+list(self.mapper.keys())[list(self.mapper.values()).index(i)])

		#print(distance)

	def get_shortest_path(self,startnode,goalnode,maxnodes):
		stopcounter=0
		self.check_row(startnode,maxnodes)
		print(self.distance)
		keystr=min(self.distance,key=lambda k:self.distance[k])
		print("min-> %s = %d"%(keystr,self.distance[keystr]))
		self.distance.pop(keystr)

		while(goalnode not in keystr):
			self.check_row(keystr,maxnodes)
			print(self.distance)
			keystr=min(self.distance,key=lambda k:self.distance[k])
			print("min-> %s = %d"%(keystr,self.distance[keystr]))
			self.distance.pop(keystr)
			stopcounter+=1
			print("stop",stopcounter)
			if stopcounter==100:
				print("NO SOLUTION FOUND")
				break

		print("A * min cost path is -> ",keystr)







a = a_star()
a.get_biginput(50,10,60)
#print(a.mapper)
start_time = t.time()
a.get_shortest_path('AA','BX',50)
print("Time taken in ->%f sec"%(t.time()-start_time))