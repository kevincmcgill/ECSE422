
numOfNodes = 6
reli = [0.94, 0.91, 0.96, 0.93, 0.92, 0.94, 0.97, 0.91, 0.92, 0.94, 0.90, 0.94, 0.93, 0.96, 0.91]
cost = [10, 25, 10, 20, 30, 10, 10, 25, 20, 20, 40, 10, 20, 10, 30]
	
class Edge:
	def __init__(self,nodeA,nodeB,reli,cost):
		self.nodeA = nodeA
		self.nodeB = nodeB
		self.reli = reli
		self.cost = cost


def main():
	edgeNum = 0
	for i in range(numOfNodes):
		edgeNum += i  

		

	edge = [None]*edgeNum
	
	z = 0


	for x in range(numOfNodes):
		for y in range(x+1,numOfNodes,1):
			e1 = Edge(x,y,reli[z],cost[z])
			edge[z] = e1
			z = z + 1

	sorted = [None]*edgeNum



	for x in range(edgeNum):
		for y in range(edgeNum):
			if y == 0 :
				pointer = 0
			elif edge[pointer].reli < edge[y].reli:
				pointer = y

		sorted[x] = edge[pointer]
		edge[pointer] = edge[x]
	
	for x in range(edgeNum):
		print(sorted[x].nodeA,sorted[x].nodeB,sorted[x].reli,sorted[x].cost)

# 	for node in range()
# 		nodesReli(6);
	

# def nodesReli(node):

# 	global numOfNodes
# 	global reli
# 	global cost
# 	temp = 0
# 	for i in range(node + 1):
# 		temp += i

# 		# print (node)
# 		# print ("output" ,((node+1)*(numOfNodes-1)-temp-1)-numOfNodes + node + 1)
# 	print("list:", end = ' ')

# 	for k in range(3,-1,-1):

# 		print( k, end = ' ')

# 	# print ()	
# 	print ((node+1)*(numOfNodes-1)-temp-1)
# 	print (((node+1)*(numOfNodes-1)-temp-1)-numOfNodes - node + 1)
# 	for k in range(((node+1)*(numOfNodes-1)-temp-1),(((node+1)*(numOfNodes-1)-temp-1)-numOfNodes + node + 2), -1 ):
# 		print ()	
		
main()