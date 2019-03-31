import doubleList as DL
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

def buildSpanningTree(list):
    i = 0
    spanningTree = DL.DoubleList()
    for i in range(len(list)):
        if i == 0: #initial edge and nodes
            spanningTree.append(list[i].nodeA)
            spanningTree.append(list[i].nodeB)
            spanningTree.show()
        else:
            # add logic
            return


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

    buildSpanningTree(edge)


if __name__ == "__main__":
    main()