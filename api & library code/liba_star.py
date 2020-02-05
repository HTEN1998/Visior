from astar_python.astar import Astar
from random import randrange
import time as t
from Testcase import *

mat=[[0,1,2,0,0,0,0,0],
			[0,0,0,7,4,0,0,0],
			[0,0,0,0,0,7,1,0],
			[0,0,0,0,0,0,0,3],
			[0,0,0,0,0,0,0,2],
			[0,0,0,0,0,0,0,5],
			[0,0,0,0,0,0,0,12],
			[0,0,0,0,0,0,0,0]]

#generating matrix



start_time = t.time()
tt = TractionTest()

astar = Astar(tt.getTestCase())
result = astar.run([0,0],[8,7])

print(result)

print("Time taken in ->%f sec"%(t.time()-start_time))