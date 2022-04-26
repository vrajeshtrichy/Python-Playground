class Array:
    def __init__(self):
        self.length = 0  # Default length
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        lastEle = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastEle

    # Wen need to delete and item and shift the indices of other items by 1
    def delete(self, index):
        itemToDelete = self.data[index]
        self.shiftItems(index)
        return itemToDelete

    def shiftItems(self, index):
        for i in range(index, self.length - 1):
            print(i)
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1

    def __str__(self):
        return str(self.__dict__)


newArray = Array()
newArray.push(1)
newArray.push(2)
newArray.push(3)
newArray.push(5)
newArray.push(6)
newArray.push(7)
newArray.push(8)

print(newArray)
newArray.pop()
print(newArray)
newArray.delete(3)
print(newArray)
