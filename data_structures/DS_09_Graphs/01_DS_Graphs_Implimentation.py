# ADJACENT LIST - We can also use any Object(like Dict) instead of Array
# Here the index is the value of the actual node and the values are the node's neighbors
# graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

class Graph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def __str__(self):
        return str(self.__dict__)

    def addVertex(self, node):
        if node not in self.adjacentList:
            self.adjacentList[node] = []
            self.numberOfNodes += 1
        return self

    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
        pass

    def showConnection(self):
        for vertex, neighbors in self.adjacentList.items():
            print(vertex, end='-->')
            print(' '.join(neighbors))


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
print(myGraph)
myGraph.showConnection()
