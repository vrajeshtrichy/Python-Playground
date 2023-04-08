# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Test case format:
#
# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with
# val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
#
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of
# neighbors of a node in the graph.
#
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference
# to the cloned graph.

# Example 1
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and
# it does not have any neighbors.

# Example 3
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.

# Constraints:
#
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given node.

# Approach 1:
# Create a new node to be returned as the copy of the input node. Assign its value to be the value of the input node.
# Create an array of visited nodes to keep track of the nodes we have already visited. Initialize the array to null.
# Add the input node to the visited array with its corresponding copied node.
# Create a queue and add the input node to the queue.
# While the queue is not empty, dequeue a node from the front of the queue and iterate through its neighbors.
# For each neighbor of the dequeued node, check if it has been visited before by checking if its corresponding
# copied node exists in the visited array. If not, create a new node and add it to the visited array with its
# corresponding copied node. Enqueue the neighbor to the queue.
# Add the copied neighbor node to the copied dequeued node's neighbors list.
# Repeat steps 5-7 until the queue is empty.
# Return the copied node.


# Approach 2:
# Create a dict for visitedNodes
# Create DFS to clone with parameter node
#   if node already in visitedNodes return the visitedNodes dict for key = node
#   Create a new Node to hold the copied data and copy the value
#   Add the new Node to the visitedNodes dict for key = node
#   For each neigh in node, pass it through the dfs and append it to the new Node
# Return the cloned node

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        visitedNodes = {}

        def dfs_traverse_clone(n: 'Node') -> 'Node':
            if n in visitedNodes: return visitedNodes[n]

            copiedNode = Node()
            copiedNode.val = n.val

            visitedNodes[n] = copiedNode

            for neighborNode in n.neighbors:
                copiedNode.neighbors.append(dfs_traverse_clone(neighborNode))

            return copiedNode

        newGraph = dfs_traverse_clone(node)
        return newGraph





        # if len(node.neighbors) == 0: return node.val
        # nNodes = node.neighbors
        # while nNodes is not None:



