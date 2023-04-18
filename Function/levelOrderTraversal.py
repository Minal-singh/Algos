from collections import deque

def levelOrderTraversal(root):
    if root is None:
        return []
    queue = deque()
    queue.append(root)
    ans = []
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(temp)
    return ans
