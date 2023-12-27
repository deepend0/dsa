# 133. Clone Graph

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        node_copy = Node(node.val)
        created_nodes = {node: node_copy}
        to_visit = [node]
        to_visit_copy = [node_copy]

        visited = set()
        while to_visit:
            visit = to_visit.pop()
            visit_copy = to_visit_copy.pop()
            if visit not in visited:
                visited.add(visit)
                for neighbor in visit.neighbors:
                    if neighbor in created_nodes:
                        neighbor_copy = created_nodes[neighbor]
                    else:
                        neighbor_copy = Node(neighbor.val)
                        created_nodes[neighbor] = neighbor_copy
                    visit_copy.neighbors.append(neighbor_copy)
                    to_visit.append(neighbor)
                    to_visit_copy.append(neighbor_copy)

        return node_copy

def print_graph(node: Node) -> Node:
        if node:
            to_visit = [node]

            visited = set()
            while to_visit:
                visit = to_visit.pop()
                if visit not in visited:
                    print(visit.val)
                    visited.add(visit)

                    for neighbor in visit.neighbors:
                        to_visit.append(neighbor)

s = Solution()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.neighbors = [n2, n3]
n2.neighbors = [n1, n3]
n3.neighbors = [n1, n2]

print("Original: ")
print_graph(n1)
print("Copy: ")
print_graph(s.cloneGraph(n1))

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

print("Original: ")
print_graph(n1)
print("Copy: ")
print_graph(s.cloneGraph(n1))



print("Original: ")
print_graph(None)
print("Copy: ")
print_graph(s.cloneGraph(None))
