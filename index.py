import doubleList as DL
import itertools
numOfNodes = 6
reliability = [0.94, 0.91, 0.96, 0.93, 0.92, 0.94, 0.97, 0.91, 0.92, 0.94, 0.90, 0.94, 0.93, 0.96, 0.91]
cost = [10, 25, 10, 20, 30, 10, 10, 25, 20, 20, 40, 10, 20, 10, 30]
edgeNum = len(reliability)

class Edge:
	def __init__(self,nodeA,nodeB,reliability,cost):
		self.nodeA = nodeA
		self.nodeB = nodeB
		self.reliability = reliability
		self.cost = cost


class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next



def decreasingReli(elem):
    return elem.reliability

def getCost(list):
    i = 0
    cost = 0
    for i in range(len(list)):
        cost = cost + list[i].cost
    return cost

# def buildSpanningTree(list):
#     i = 0
#     spanningTree = DL.DoubleList()
#     for i in range(len(list)):
#         if i == 0: #initial edge and nodes
#             spanningTree.append(list[i].nodeA)
#             spanningTree.append(list[i].nodeB)
#             spanningTree.show()
#         else:
#             # add logic
#             return

def getReli(edge):
    # print("")

    # for x in range(len(edge)):
    #     print("Edge #", x+1, ":", edge[x].nodeA,"-", edge[x].nodeB, "Reliability:",edge[x].reliability, "Cost:", edge[x].cost)

    # create an array with edgeNumber
    edgeNumber = range(len(edge))
    # to connect N nodes, we need at least N-1 edges
    # find all combination with N-1 edges (all kind of possible minimal spanning tree)
    # combination = list(combinations(edgeNumber,numOfNodes -1 ))
    combination = list(itertools.product([0, 1], repeat = len(edge)))

    i = 0
    while True:
        if i == (len(combination) - 1):
            break 
        elif sum(combination[i]) < numOfNodes-1:
            del combination[i]
        else:
            i += 1
    
    outputReliability = 0
    # print(len(combination))

    for i in range(len(combination)):
   
        # declare an empty array to store connected nodes
        connectedNode = []
        offReliability = 1
        
        subGraph = []
        for j in range(len(edge)):
            if combination[i][j] == 1: 
                subGraph.append(edge[j])
                 
        if not isAllConnected(subGraph):
            continue


        # put all connected node in this combination into connectedNode array
        subGraphReliability = 1
        for j in range(len(combination[0])):
            # if that edge is on 
            if combination[i][j] == 1: 
                subGraphReliability *= edge[j].reliability
            # if the edge is off
            else:
                 subGraphReliability *= (1 - edge[j].reliability)

        print("reli", subGraphReliability)
        outputReliability += subGraphReliability


    return outputReliability

def isAllConnected(edge):

    # check if all is connected
    connectedNode = []
    # starting from 1
    connectedNode.append(1)
    i = 0
    while i < numOfNodes:
        if len(connectedNode) <= i:
            return False
        if len(connectedNode) == numOfNodes:
            return True
        for x in range(len(edge)):
            
            if edge[x].nodeA == connectedNode[i] and edge[x].nodeB not in connectedNode: 
                connectedNode.append(edge[x].nodeB)

            if edge[x].nodeB == connectedNode[i] and edge[x].nodeA not in connectedNode:
                connectedNode.append(edge[x].nodeA)
        i += 1

def buildSpanningTree(edge):
    connectedNode = []
    pickedEdge = []
    i = 0
    while len(connectedNode) < numOfNodes:
        if i == 0:
            pickedEdge.append(edge[i])
            connectedNode.append(edge[i].nodeA)
            connectedNode.append(edge[i].nodeB)


        elif edge[i].nodeA in connectedNode and edge[i].nodeB in connectedNode:
            i += 1
            continue

        else:
            pickedEdge.append(edge[i])
            if edge[i].nodeA not in connectedNode:
                connectedNode.append(edge[i].nodeA)
            if edge[i].nodeB not in connectedNode:
                connectedNode.append(edge[i].nodeB)
        i += 1
    return pickedEdge



def main():
    edge = [None] * edgeNum
    z = 0
    # Create edge array
    for x in range(numOfNodes):
        for y in range(x + 1, numOfNodes, 1):
            edge[z] = Edge(x+1, y+1, reliability[z], cost[z])
            z = z + 1

    edge.sort(key=decreasingReli, reverse=True)

    for x in range(edgeNum):
        print("Edge #", x+1, ":", edge[x].nodeA,"-", edge[x].nodeB, "Reliability:",edge[x].reliability, "Cost:", edge[x].cost)

    print("Total cost:", getCost(edge))

    #build minimal spanning tree
    spanningTreeEdge = buildSpanningTree(edge)
    # for x in range(len(spanningTreeEdge)):
    #     print("Edge #", x+1, ":", spanningTreeEdge[x].nodeA,"-", spanningTreeEdge[x].nodeB, "Reliability:",spanningTreeEdge[x].reliability, "Cost:", spanningTreeEdge[x].cost)
    # print("Total cost:", getCost(spanningTreeEdge))

    testSet = [edge[0],edge[1],edge[2],edge[4],edge[5],edge[7],edge[11]]
    for x in range(len(testSet)):
        print("Edge #", x+1, ":     ", testSet[x].nodeA,"-", testSet[x].nodeB, "        Reliability:",testSet[x].reliability, "Cost:", testSet[x].cost)

    # print(getReli(spanningTreeEdge))
    print(getReli(edge))
    # print(getReli(edge))


if __name__ == "__main__":
    main()