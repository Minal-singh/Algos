from heapq import *

def dijkstra(n, graph, node1, node2):
    # n: number of nodes
    # graph: adjacency matrix
    # node1: start node
    # node2: end node
    # return: shortest path from node1 to node2
    #         and the length of the path

    # initialize
    heap = [] # heap
    heappush(heap, [0, node1]) # push the start node into the heap
    dist = [float("inf")] * n
    dist[node1] = 0

    # find the shortest path
    while heap:
        d, u = heappop(heap)
        if u == node2:
            return d
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(heap, [dist[v], v])
    return -1
