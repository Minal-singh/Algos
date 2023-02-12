class FenwickTree:

    def __init__(self, arr):
        self.arr = arr
        self.fenwickTree = [0] + arr
        self.size = len(arr) + 1
        self.__build()

    def __prev(self, n):
        return n - (n&-n)

    def __next(self, n):
        return n + (n&-n)

    def __build(self):
        for index in range(1, self.size):
            tempIndex = self.__next(index)
            while(tempIndex < self.size):
                self.fenwickTree[tempIndex] += self.arr[index-1]
                tempIndex = self.__next(tempIndex)

    def pointUpdate(self, index, val):
        delta = val - self.arr[index-1]
        while(index < self.size):
            self.fenwickTree[index] += delta
            index = self.__next(index)

    def pointQuery(self, index) -> int: #1 based indexing
        ans = 0
        while(index > 0):
            ans += self.fenwickTree[index]
            index = self.__prev(index)
        return ans

    def rangeQuery(self, startIndex, endIndex) -> int: #1 based indexing and both inclusive
        ans = 0
        ans += self.pointQuery(endIndex)
        ans -= self.pointQuery(startIndex - 1)
        return ans
