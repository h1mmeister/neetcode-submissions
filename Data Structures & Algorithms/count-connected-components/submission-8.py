class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_of_connected_components = 0
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [False] * n

        def bfs(node):
            queue = deque()
            queue.append(node)

            while queue:
                curr_node = queue.popleft()
                for neighbor in adj_list[curr_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                num_of_connected_components += 1
                bfs(node)

        return num_of_connected_components


        