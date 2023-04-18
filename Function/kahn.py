from collections import deque

def kahn(graph):
    # graph: adjacency list
    # return: topological order of the graph
    #         or -1 if the graph is not a DAG

    # initialize
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    # find the topological order
    queue = deque()
    queue.extend([u for u in range(n) if in_degree[u] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    if len(order) == n:
        return order
    return -1
