# import doubleList as DL
import itertools

# create by Mei Tang (260742835) and Kevin Chen (260658680) for ECSE 422 project
# 


numOfNodes = 6
reliability = [0.94, 0.91, 0.96, 0.93, 0.92, 0.94, 0.97, 0.91, 0.92, 0.94, 0.90, 0.94, 0.93, 0.96, 0.91]
cost = [10, 25, 10, 20, 30, 10, 10, 25, 20, 20, 40, 10, 20, 10, 30]
# if costGoal is negative, the cost constrain = infinity (no cost constain)
costGoal = 100
reliabilityGoal = 0.9


edgeNum = len(reliability)
class Edge:
	def __init__(self,nodeA,nodeB,reliability,cost):
		self.nodeA = nodeA
		self.nodeB = nodeB
		self.reliability = reliability
		self.cost = cost


# class Node:
#     def __init__(self, data, prev, next):
#         self.data = data
#         self.prev = prev
#         self.next = next



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
    # to connect N nodes, we need at least N-1 edges
    # find all combination with N-1 edges (all kind of possible minimal spanning tree)
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
    for i in range(len(combination)):
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


def meetReliabilityGoal(edge):
    
    # to connect N nodes, we need at least N-1 edges
    # find all combination with N-1 edges (all kind of possible minimal spanning tree)
    combination = list(itertools.product([0, 1], repeat = len(edge)))

    graphSet = []
    i = 0
    while True:
        if i == (len(combination) - 1):
            break 
        elif sum(combination[i]) < numOfNodes-1:
            del combination[i]
        else:
            i += 1

    for i in range(len(combination)):
   
        # declare an empty array to store connected nodes
        connectedNode = []
        offReliability = 1
        
        graph = []
        for j in range(len(edge)):
            if combination[i][j] == 1: 
                graph.append(edge[j])
                 
        if not isAllConnected(graph):
            continue

        if costGoal > 0:
            if getCost(graph) > costGoal:
                continue

        if getReli(graph) >= reliabilityGoal:
            graphSet.append(graph)
            # if len(graphSet) == 210:
            #       return graphSet
    return graphSet

def findMaxReliability(graphSet):
    outputGraph = []
    MaxReli = 0
    for x in range(len(graphSet)):
        if getReli(graphSet[x]) > MaxReli:
            outputGraph = graphSet[x]
            MaxReli = getReli(graphSet[x])

    print("")

    for x in range(len(outputGraph)):
        print("Edge #", x+1, ":", outputGraph[x].nodeA,"-", outputGraph[x].nodeB, "Reliability:",outputGraph[x].reliability, "Cost:", outputGraph[x].cost)
    print("Total cost:", getCost(outputGraph))
    print("Best Reliability", getReli(outputGraph)) 


# !!!!!!!!!! IMPORTANT !!!!!!!!!!!!
# DO NOT put a large value as the cost constain. 
# This will make the system run so slow


def main():
    edge = [None] * edgeNum
    z = 0
    # Create edge array
    for x in range(numOfNodes):
        for y in range(x + 1, numOfNodes, 1):
            edge[z] = Edge(x+1, y+1, reliability[z], cost[z])
            z = z + 1

    edge.sort(key=decreasingReli, reverse=True)

    # for x in range(edgeNum):
    #     print("Edge #", x+1, ":", edge[x].nodeA,"-", edge[x].nodeB, "Reliability:",edge[x].reliability, "Cost:", edge[x].cost)

    # print("Total cost:", getCost(edge))

    #build minimal spanning tree
    # spanningTreeEdge = buildSpanningTree(edge)
    # for x in range(len(spanningTreeEdge)):
    #     print("Edge #", x+1, ":", spanningTreeEdge[x].nodeA,"-", spanningTreeEdge[x].nodeB, "Reliability:",spanningTreeEdge[x].reliability, "Cost:", spanningTreeEdge[x].cost)
    # print("Total cost:", getCost(spanningTreeEdge))
    


    # all graph that meet the constrain
    sol = meetReliabilityGoal(edge)
    print(50* "*")
    print("PART a) Solutions meeting reliability goal: ", reliabilityGoal, "\n")
    # print out the entire set
    for x in range(len(sol)):
        print("Solution #",x+1)
        print("Total reliability:",getReli(sol[x]))
        for i in range(len(sol[x])):
            print("Edge #", i+1, ":", sol[x][i].nodeA,"-", sol[x][i].nodeB, "Reliability:",sol[x][i].reliability, "Cost:", sol[x][i].cost)
        print("")

    print(50 * "*")
    print("PART b) Solutions meeting reliability goal: ", reliabilityGoal, "given cost constraint:", costGoal, "\n")
    print(50 * "*")
    print("PART c) Solution with maximum reliability given cost constraint:", costGoal)
    # find the max reliability in given constrain
    findMaxReliability(sol)
    print(50 * "*")
    


if __name__ == "__main__":
    main()