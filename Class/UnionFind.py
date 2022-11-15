class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)
        self.size = [1] * (size + 1)

    def findParent(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def isSameComponent(self, u, v):
        par_u = self.findParent(u)
        par_v = self.findParent(v)
        return par_u == par_v

    def unionByRank(self, u, v):
        if not self.isSameComponent(u, v):
            par_u = self.parent[u]
            par_v = self.parent[v]
            if self.rank[par_u] < self.rank[par_v]:
                self.parent[par_u] = par_v
            elif self.rank[par_v] < self.rank[par_u]:
                self.parent[par_v] = par_u
            else:
                self.parent[par_u] = par_v
                self.rank[par_v] += 1

    def unionBySize(self, u, v):
        if not self.isSameComponent(u, v):
            par_u = self.parent[u]
            par_v = self.parent[v]
            if self.size[par_u] < self.size[par_v]:
                self.parent[par_u] = par_v
                self.size[par_v] += self.size[par_u]
            else:
                self.parent[par_u] = par_v
                self.size[par_v] += self.size[par_u]


ds = UnionFind(7)
ds.unionByRank(1, 2)
ds.unionByRank(2, 3)
ds.unionByRank(4, 5)
ds.unionByRank(6, 7)
ds.unionByRank(5, 6)
print(ds.isSameComponent(3, 7))
ds.unionByRank(3, 7)
print(ds.isSameComponent(3, 7))

ds2 = UnionFind(7)
ds2.unionBySize(1, 2)
ds2.unionBySize(2, 3)
ds2.unionBySize(4, 5)
ds2.unionBySize(6, 7)
ds2.unionBySize(5, 6)
print(ds2.isSameComponent(3, 7))
ds2.unionBySize(3, 7)
print(ds2.isSameComponent(3, 7))
