class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        ranks = [0] * n

        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def union(node1, node2):
            node1_repr = find(node1)
            node2_repr = find(node2)

            if node1_repr == node2_repr:
                return 0

            if ranks[node1_repr] > ranks[node2_repr]:
                parents[node2_repr] = node1_repr
            elif ranks[node1_repr] < ranks[node2_repr]:
                parents[node1_repr] = node2_repr
            else:
                parents[node2_repr] = node1_repr
                ranks[node1_repr] += 1

            return 1

        num_of_components = n
        for u, v in edges:
            num_of_components -= union(u, v)

        return num_of_components
        