"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
from collections import deque


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here

        if root is None:
            return []

        result = []
        queue = deque([root])
        dummy = ListNode(0)  # 0->None
        lastNode = None
        while queue:
            lastNode = dummy
            for _ in range(len(queue)):
                node = queue.popleft()
                lastNode.next = ListNode(node.val)  # point to the value
                lastNode = lastNode.next  # move
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(dummy.next)
        return result
