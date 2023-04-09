class SGTree:

    def __init__(self, arr):
        self.size = len(arr)
        self.arr = arr
        self.seg = [0]*(self.size * 4 + 1)

    def build(self, index, low, high):
        if low == high:
            self.seg[index] = self.arr[low]
            return

        mid = (low+high)//2
        self.build(index*2+1, low, mid)
        self.build(index*2+2, mid+1, high)
        self.seg[index] = min(self.seg[index*2+1], self.seg[index*2+2])

    def query(self, index, low, high, l, r):
        if r<low or l>high:
            return float('inf')

        if low>=l and high<=r:
            return self.seg[index]

        mid = (low+high)//2
        return min(self.query(index*2+1, low, mid,l,r), self.query(index*2+2, mid+1, high,l,r))

    def update(self, index, low, high, indx, val):
        if low == high:
            self.seg[index] = val
            self.arr[indx] = val
            return
        mid = (low+high)//2
        if indx<=mid:
            self.update(index*2+1, low, mid, indx, val)
        else:
            self.update(index*2+2, mid+1, high, indx, val)
        self.seg[index] = min(self.seg[index*2+1], self.seg[index*2+2])

n = int(input())
arr = list(map(int, input().split()))

sgt = SGTree(arr)
sgt.build(0, 0, n-1)

q = int(input())
ans = []
for _ in range(q):
    l,r = map(int,input().split())
    ans.append([l, r, min(sgt.query(0, 0, n-1, 0, l-2), sgt.query(0, 0, n-1, r, n-1), n)])
print(ans)
