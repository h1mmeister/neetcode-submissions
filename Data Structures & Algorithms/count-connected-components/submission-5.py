class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        num_of_connected_componenets = 0
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # visited = [False for _ in range(n)]
        visited = [False] * n

        for node in range(n):
            if not visited[node]:
                visited[node] = True
                num_of_connected_componenets += 1
                stack = []
                stack.append(node)

                while stack:
                    curr_node = stack.pop()
                    for neighbor in adj_list[curr_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

        return num_of_connected_componenets



        