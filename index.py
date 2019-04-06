import itertools

# created by Mei Tang (260742835) and Kevin Chen (260658680) for ECSE 422 project

# numOfNodes = 6
# reliability = [0.94, 0.91, 0.96, 0.93, 0.92, 0.94, 0.97, 0.91, 0.92, 0.94, 0.90, 0.94, 0.93, 0.96, 0.91]
# cost = [10, 25, 10, 20, 30, 10, 10, 25, 20, 20, 40, 10, 20, 10, 30]
# if costGoal is negative, the cost constrain = infinity (no cost constaint)
# costGoal = 0
# reliabilityGoal = 0

class Edge:
	def __init__(self,nodeA,nodeB,reliability,cost):
		self.nodeA = nodeA
		self.nodeB = nodeB
		self.reliability = reliability
		self.cost = cost


def runPart(file, numOfNodes, reliability,cost, edgeNum):
    outputFile = open(file, "w")
    outputFile.write("Number of Nodes: " + str(numOfNodes) + "\n")
    outputFile.write("Reliability Matrix: " + str(reliability) + "\n")
    outputFile.write("Cost Matrix: " + str(cost) + "\n")
    outputFile.write("Number of edges: " + str(edgeNum) + "\n")
    outputFile.close()


def readInputFile(answer_list):
    lines = [line for line in open('input.txt') if not line.startswith('#') and
             len(line.strip())]
    numOfNodes = int(lines[0].split("\n")[0])
    reliability = list(map(float, lines[1].split("\n")[0].split(" ")))
    cost = list(map(float, lines[2].split("\n")[0].split(" ")))
    edgeNum = len(reliability)

    print("Number of Nodes:", numOfNodes)
    print("Reliability Matrix:" , reliability)
    print("Cost Matrix:" , cost)
    print("Number of edges:", edgeNum)

    if answer_list[0]:
        runPart("resultPartA.txt",numOfNodes, reliability,cost, edgeNum)
        print("running A")

    if answer_list[1]:
        runPart("resultPartB.txt",numOfNodes, reliability,cost, edgeNum)
        print("running B")

    if answer_list[2]:
        runPart("resultPartC.txt",numOfNodes, reliability,cost, edgeNum)
        print("running C")

    return [numOfNodes, reliability, cost, edgeNum]


def decreasingReli(elem):
    return elem.reliability


def getCost(list):
    i = 0
    cost = 0
    for i in range(len(list)):
        cost = cost + list[i].cost
    return cost


def getReli(edge, numOfNodes):
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
                 
        if not isAllConnected(subGraph, numOfNodes):
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


def isAllConnected(edge, numOfNodes):

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


def buildSpanningTree(edge, numOfNodes):
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


def meetReliabilityGoal(edge, numOfNodes, reliabilityGoal, costGoal, costContrained):
    
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
                 
        if not isAllConnected(graph, numOfNodes):
            continue

        if costContrained and costGoal > 0:
            if getCost(graph) > costGoal:
                continue

        if getReli(graph, numOfNodes) >= reliabilityGoal:
            graphSet.append(graph)
            # if len(graphSet) == 210:
            #       return graphSet
    return graphSet

def findMaxReliability(outputFile, graphSet, numOfNodes):
    outputGraph = []
    MaxReli = 0
    for x in range(len(graphSet)):
        if getReli(graphSet[x], numOfNodes) > MaxReli:
            outputGraph = graphSet[x]
            MaxReli = getReli(graphSet[x], numOfNodes)

    outputFile.write("\n")

    for x in range(len(outputGraph)):
        outputFile.write("Edge # " + str(x+1) + " : " + str(outputGraph[x].nodeA) + " - " + str(outputGraph[x].nodeB) + " Reliability: " + str(outputGraph[x].reliability) + " Cost: " + str(outputGraph[x].cost) + "\n")
    outputFile.write("Total cost: " + str(getCost(outputGraph)) + "\n")
    outputFile.write("Max Reliability " + str(getReli(outputGraph,numOfNodes)) + "\n")

def printSolutions(file,sol, numOfNodes):
    for x in range(len(sol)):
        file.write("Solution # " + str(x+1) + "\n")
        file.write("Total reliability:" + str(getReli(sol[x], numOfNodes)) + "\n")
        for i in range(len(sol[x])):
            file.write("Edge # " + str(i+1) + ": " + str(sol[x][i].nodeA) + " - " + str(sol[x][i].nodeB) + " Reliability: " + str(sol[x][i].reliability) + " Cost: " + str(sol[x][i].cost) + "\n")
        file.write("\n")


# !!!!!!!!!! IMPORTANT !!!!!!!!!!!!
# DO NOT put a large value as the cost constain. 
# This will make the system run so slow


def main():
    reliabilityGoal = float(input("Please enter reliability goal (from 0 to 1): "))
    costGoal = int(input("Please enter cost constraint (from 1 to 100): "))

    runPartA = input("Would you like to run part A? (y/n)")
    runPartB = input("Would you like to run part B? (y/n)")
    runPartC = input("Would you like to run part C? (y/n)")

    answer_list = []
    for answer in [runPartA, runPartB, runPartC]:
        if answer == "y" or answer == "Y" or answer == "yes" or answer == "Yes" or answer == "YES":
            answer = True
        else:
            answer = False
        answer_list.append(answer)

    print(50 * "*")
    print("Reliability goal set to: " + str(reliabilityGoal))
    print("Cost constraint set to: " + str(costGoal))
    inputValues = readInputFile(answer_list)
    numOfNodes = inputValues[0]
    reliability = inputValues[1]
    cost = inputValues[2]
    edgeNum = inputValues[3]

    edge = [None] * edgeNum
    z = 0
    # Create edge array
    for x in range(numOfNodes):
        for y in range(x + 1, numOfNodes, 1):
            edge[z] = Edge(x+1, y+1, reliability[z], cost[z])
            z = z + 1

    edge.sort(key=decreasingReli, reverse=True)

    # Execute Part A
    if answer_list[0]:
        outputFileA = open("resultPartA.txt", "a")
        outputFileA.write(50 * "*" + "\n")
        outputFileA.write("PART a) Solutions meeting reliability goal: " + str(reliabilityGoal) + "\n")
        solA = meetReliabilityGoal(edge, numOfNodes, reliabilityGoal, costGoal, False)
        printSolutions(outputFileA, solA, numOfNodes)
        outputFileA.write(50 * "*" + "\n")
        outputFileA.close()

    # Execute Part B
    solB = None
    if answer_list[1]:
        outputFileB = open("resultPartB.txt", "a")
        outputFileB.write(50 * "*" + "\n")
        outputFileB.write(
            "PART b) Solutions meeting reliability goal: " + str(reliabilityGoal) + " given cost constraint: " + str(
                costGoal) + "\n")
        solB = meetReliabilityGoal(edge, numOfNodes, reliabilityGoal, costGoal, True)
        printSolutions(outputFileB, solB, numOfNodes)
        outputFileB.write(50 * "*" + "\n")
        outputFileB.close()

    # Execute Part C
    if answer_list[2]:
        if solB is None:
            solB = meetReliabilityGoal(edge, numOfNodes, reliabilityGoal, costGoal, True)
        outputFileC = open("resultPartC.txt", "a")
        outputFileC.write(50 * "*" + "\n")
        outputFileC.write("PART c) Solution for maximum reliability given cost constraint: " + str(costGoal) + "\n")
        findMaxReliability(outputFileC, solB, numOfNodes)
        outputFileC.write(50 * "*" + "\n")
        outputFileC.close()


if __name__ == "__main__":
    main()