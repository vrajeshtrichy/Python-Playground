from DS_Queue_LL_Implimentation import Queue
from collections import deque


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        parent = self.traverseTo(value)
        # print('parent', parent.value)
        if value < parent.value:
            parent.left = newNode
        else:
            parent.right = newNode
        return self

    def traverseTo(self, value):
        currentNode = self.root
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    return currentNode
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    return currentNode
                else:
                    currentNode = currentNode.right

    def lookup(self, value):
        if self.root is None:
            return None
        currentNode = self.root
        while currentNode is not None:
            if value == currentNode.value:
                return str(value) + ' is FOUND'
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return str(value) + ' is Not FOUND'

    # NOT WORKING, NEED TO FIX
    def remove(self, value):
        if self.root == None:
            return False

        currentNode = self.root
        parentNode = None

        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value == currentNode.value:
                # We have a match, get to work!

                # Option 1: No right child:
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        # if parent < current value, make left child a right child of parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left

                # Option 2: Right child which doesnt have a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        # //if parent > current, make right child of the left the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        # //if parent < current, make right child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right


                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
            return True

    def printt(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next
        print('\nLength ' + str(self.length) + '\n')

    def breadthFirstSearch_bk(self):
        currentNode = self.root
        bfsList = []
        queue = Queue()
        queue.enqueue(currentNode)
        while not queue.isEmpty():
            currentNode = queue.dequeue()
            bfsList.append(currentNode.value)
            if currentNode.left is not None:
                queue.enqueue(currentNode.left)
            if currentNode.right is not None:
                queue.enqueue(currentNode.right)

        return bfsList

    def breadthFirstSearch(self):
        currentNode = self.root
        bfsList = []
        queue = deque([])
        queue.append(currentNode)
        while len(queue) > 0:
            currentNode = queue.popleft()
            bfsList.append(currentNode.value)
            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

        return bfsList

    def breadthFirstSearch_R(self, queue, bfsList):
        if len(queue) == 0:
            return bfsList

        # print('bfslist-', bfsList)

        currentNode = queue.popleft()
        bfsList.append(currentNode.value)
        if currentNode.left is not None:
            queue.append(currentNode.left)
            # print('qL-', currentNode.left.value)
        if currentNode.right is not None:
            queue.append(currentNode.right)
            # print('qR-', currentNode.right.value)

        return self.breadthFirstSearch_R(queue, bfsList)

    def dfsInOrder(self):
        '''
        :return: 1, 4, 6, 9, 15, 20, 170
        '''
        return self.traverseInOrder_R(self.root, [])

    def traverseInOrder_R(self, node, list):
        if node.left is not None:
            self.traverseInOrder_R(node.left, list)
        list.append(node.value)
        if node.right is not None:
            self.traverseInOrder_R(node.right, list)
        return list

    def dfsPreOrder(self):
        '''
        :return: 9, 4, 1, 6, 20, 15, 170
        '''
        return self.traversePreOrder_R(self.root, [])

    def traversePreOrder_R(self, node, list):
        list.append(node.value)
        if node.left is not None:
            self.traversePreOrder_R(node.left, list)
        if node.right is not None:
            self.traversePreOrder_R(node.right, list)
        return list

    def dfsPostOrder(self):
        '''
        :return: 1, 6, 4, 15, 170, 20, 9
        '''
        return self.traversePostOrder_R(self.root, [])

    def traversePostOrder_R(self, node, list):
        if node.left is not None:
            self.traversePostOrder_R(node.left, list)
        if node.right is not None:
            self.traversePostOrder_R(node.right, list)
        list.append(node.value)
        return list

#             9
#        4         20
#     1    6    15    170

def traverse(node):
    treeDict = {'value': node.value}
    treeDict['left'] = None if node.left is None else traverse(node.left)
    treeDict['right'] = None if node.right is None else traverse(node.right)
    return treeDict


tree = BinarySearchTree()
tree.insert(9)
# print(traverse(tree.root))
tree.insert(4)
# print(traverse(tree.root))
tree.insert(6)
# print(traverse(tree.root))
tree.insert(20)
# print(traverse(tree.root))
tree.insert(170)
# print(traverse(tree.root))
tree.insert(15)
# print(traverse(tree.root))
tree.insert(1)
print(traverse(tree.root))
print(tree.lookup(13))
print(tree.lookup(170))
tree.remove(20)
print(traverse(tree.root))
print('breadthFirstSearch: ', tree.breadthFirstSearch())
print('breadthFirstSearch_Rec: ',
      tree.breadthFirstSearch_R(deque([tree.root]), []))
print('DFS Inorder: ', tree.dfsInOrder())
print('DFS Preorder: ', tree.dfsPreOrder())
print('DFS Postorder: ', tree.dfsPostOrder())
