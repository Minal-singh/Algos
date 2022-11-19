class SGTree:
    def __init__(self, size) -> None:
        self.seg = [0] * (4 * size + 1)
        self.lazy = [0] * (4 * size + 1)

    def bulid(self, ind, low, high, arr):
        if low == high:
            self.seg[ind] = arr[low]
            return

        mid = (low + high) // 2
        self.build(ind * 2 + 1, low, mid, arr)
        self.build(ind * 2 + 2, mid + 1, high, arr)
        self.seg[ind] = max(self.seg[ind * 2 + 1], self.seg[ind * 2 + 2])

    def query(self, ind, low, high, l, r):
        if self.lazy[ind] != 0:
            self.seg[ind] += self.lazy[ind]
            if low != high:
                self.lazy[2 * ind + 1] += self.lazy[ind]
                self.lazy[2 * ind + 2] += self.lazy[ind]
            self.lazy[ind] = 0

        if l > high or r < low:
            return -float("inf")

        if l <= low and r >= high:
            return self.seg[ind]

        mid = (low + high) // 2
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return max(left, right)

    def update(self, ind, low, high, l, r, val):
        if self.lazy[ind] != 0:
            self.seg[ind] += self.lazy[ind]
            if low != high:
                self.lazy[2 * ind + 1] += self.lazy[ind]
                self.lazy[2 * ind + 2] += self.lazy[ind]
            self.lazy[ind] = 0

        # no overlap
        if low > r or high < l:
            return

        # complete overlap
        if low >= l and high <= r:
            self.seg[ind] += val
            if low != high:
                self.lazy[2 * ind + 1] += val
                self.lazy[2 * ind + 2] += val
            return

        # partial overlap
        mid = (low + high) // 2
        self.update(ind * 2 + 1, low, mid, l, r, val)
        self.update(ind * 2 + 2, mid + 1, high, l, r, val)
        self.seg[ind] = max(self.seg[ind * 2 + 1], self.seg[ind * 2 + 2])
