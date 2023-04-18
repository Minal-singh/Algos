# morris traversal of a binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []
        while root:
            if root.left:
                # find the predecessor of root
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    result.append(root.val)
                    predecessor.right = None
                    root = root.right
            else:
                result.append(root.val)
                root = root.right
        return result
