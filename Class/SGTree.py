class SGTree:
    def __init__(self, size) -> None:
        self.seg = [0] * (4 * size + 1)

    def build(self, ind, low, high, arr) -> None:
        if low == high:
            self.seg[ind] = arr[low]
            return

        mid = (low + high) // 2
        self.build(ind * 2 + 1, low, mid, arr)
        self.build(ind * 2 + 2, mid + 1, high, arr)
        self.seg[ind] = max(self.seg[ind * 2 + 1], self.seg[ind * 2 + 2])

    def query(self, ind, low, high, l, r):
        if l > high or r < low:
            return -float("inf")

        if l <= low and r >= high:
            return self.seg[ind]

        mid = (low + high) // 2
        left = self.query(2 * ind + 1, low, mid, l, r)
        right = self.query(2 * ind + 2, mid + 1, high, l, r)
        return max(left, right)

    def update(self, ind, low, high, i, val):
        if low == high:
            self.seg[ind] = val
            return

        mid = (low + high) // 2
        if i <= mid:
            self.update(2 * ind + 1, low, mid, i, val)
        else:
            self.update(2 * ind + 2, mid + 1, high, i, val)
        self.seg[ind] = max(self.seg[2 * ind + 1], self.seg[2 * ind + 2])
