class HashTable:
    # init method initializes the size of the HasTable and the hashmap array of arrays
    def __init__(self, size):
        self.bucketSize = size
        self.hashmap = [[] for _ in range(self.bucketSize)]

    # __hash method - generates the hash value for the key
    # __ makes the method Private
    def __hash_simple(self, key):
        """
        The Load factor is a measure that decides when to increase the HashMap capacity to maintain the get() and
        put() operation complexity of O(1).

        The default load factor of HashMap is 0.75f (75% of the map size).

        Load Factor = (n/k) where
        n is the number of max number of elements that can be stored dict
        k is the bucket size

        Optimal Load factor is around (2/3) such that the effect of hash collisions is minimum
        """
        return len(str(key)) % self.bucketSize

    def __hash(self, key):
        hash = 0
        for i in range(len(str(key))):
            hash = (hash + (ord(str(key)[i]) * i)) % self.bucketSize
        return hash

    def put(self, key, value):
        address = self.__hash(key)  # Address is the ID
        self.hashmap[address].append([key, value])
        # if len(self.hashmap[address]) == 0:
        #
        #     self.hashmap[address].append([key, value])
        #     return True
        # else:
        #     self.hashmap[address].append([key, value])
        # return False

    def get(self, key):
        address = self.__hash(key)  # Address is the ID
        currentBucket = self.hashmap[address]
        print(currentBucket)
        if len(currentBucket) > 0:
            for item in currentBucket:  # O(1) - When no collision there is always single loop iteration
                if item[0] == key:
                    return item[1]
        else:
            return None

    def delete(self, key):
        address = self.__hash(key)  # Address is the ID
        currentBucket = self.hashmap[address]
        print(currentBucket)
        if len(currentBucket) > 0:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    del self.hashmap[address][i]
                    return True
        else:
            return False

    def keys(self):
        keysList = []
        bucketList = []
        for bucket in self.hashmap:
            if len(bucket) > 0:
                bucketList.extend(bucket)
        if len(bucketList) > 0:
            for item in bucketList:
                keysList.append(item[0])
            return keysList
        return None

    def __str__(self):
        return str(self.__dict__)


hashtable = HashTable(3)
hashtable.put('grapes', 10000)
hashtable.put('grass', 10)
hashtable.put('apple', 10)
hashtable.put('banana', 10)
print(hashtable)
print(hashtable.get('as'))
print(hashtable.get('apple'))
print(hashtable.delete('banana'))
print(hashtable)
print(hashtable.keys())
