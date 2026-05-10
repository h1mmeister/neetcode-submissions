class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        num_of_connected_components = 0

        for node in range(0, n):
            if node not in visited:
                num_of_connected_components += 1
                self.dfs(node, graph, visited)

        return num_of_connected_components


    def dfs(self, node, graph, visited):
        visited.add(node)

        for cn in graph[node]:
            if cn not in visited:
                self.dfs(cn, graph, visited)




        