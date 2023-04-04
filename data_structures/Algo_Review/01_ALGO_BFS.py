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