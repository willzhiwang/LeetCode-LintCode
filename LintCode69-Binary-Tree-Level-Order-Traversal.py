"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                print("node value", node.val, "----")
                level.append(node.val)
                if node.left:
                    print("Append node.left: ", node.left.val)
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    print("Append node.right: ", node.right.val)
            result.append(level)
        return result