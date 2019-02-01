# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}
        hash = {}
        # bfs
        queue = [node]
        new_root = UndirectedGraphNode(node.label)
        hash[node] = new_root
        visited[node] = True
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur not in hash:
                hash[cur] = UndirectedGraphNode(cur.label)
            
            for n in cur.neighbors:
                if n not in hash:
                    hash[n] = UndirectedGraphNode(n.label)
                hash[cur].neighbors.append(hash[n])
                if n not in visited:
                    visited[n] = True
                    queue.append(n)       
        return new_root         



s = Solution()
node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node0.neighbors = [node1, node2]
node1.neighbors = [node2]
node2.neighbors = [node2]
s.cloneGraph(node0)
s.cloneGraph(None)