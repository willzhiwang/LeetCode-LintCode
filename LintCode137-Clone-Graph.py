"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return node
        root = node
        queue = deque([node])
        nodes = set([node])
        # BFS get all nodes
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in nodes:
                    nodes.add(neighbor)
                    queue.append(neighbor)

        result = {}
        # copy nodes by using the method provided
        for node in nodes:
            result[node] = UndirectedGraphNode(node.label)

        # copy neighbors(edges)
        for node in nodes:
            new_node = result[node]
            for neighbor in node.neighbors:
                new_neighbor = result[neighbor]
                new_node.neighbors.append(new_neighbor)
        # print (result[root])
        return result[root]



