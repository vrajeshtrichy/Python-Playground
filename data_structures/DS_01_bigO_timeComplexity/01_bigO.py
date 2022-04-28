def findNemo(array):
    for i in array:
        if i == 'nemo':
            print('Found NEMO!')


def getHeader(array):
    print(array[0])


def getHeaderadnTail(array):
    print(array[0], array[-1])


def anotherFunction():
    pass


def funChallenge(input):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in range(len(input)):
        anotherFunction()  # O(n)
        stranger = True  # O(n)
        a += 1  # O(n)
    return a  # O(1)


if __name__ == '__main__':
    fishesArray = ['nemo'] * 10
    findNemo(fishesArray)  # O(n) --> Linear Time
    getHeader(fishesArray)  # O(1) --> Constant Time
    getHeaderadnTail(fishesArray)  # O(2) --> Constant Time
    funChallenge(fishesArray)  # O(3 + 4n)
