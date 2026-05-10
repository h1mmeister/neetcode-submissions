class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)

        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)

        visited = set()
        num_of_connected_components = 0

        for node in range(0, n):
            if node not in visited:
                num_of_connected_components += 1
                self.bfs(node, graph, visited)

        return num_of_connected_components


    def bfs(self, node, graph, visited):
        visited.add(node)

        queue = []
        queue.append(node)

        while queue:
            curr_node = queue.pop(0)

            for cn in graph[curr_node]:
                if cn not in visited:
                    visited.add(cn)
                    queue.append(cn)


        