class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = {node:[] for node in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj_list[i].append((cost, j))
                adj_list[j].append((cost, i))

        visited = set()
        min_cost = 0
        min_heap = [(0,0)]

        while len(visited) < len(points):
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            min_cost += curr_cost

            for neighbor_cost, neighbor_node in adj_list[curr_node]:
                if neighbor_node not in visited:
                    heapq.heappush(min_heap, (neighbor_cost, neighbor_node))

        return min_cost
        