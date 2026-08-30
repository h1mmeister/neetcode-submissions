import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_list = defaultdict(list)

        for source, target, time in times:
            edge_list[source].append((target, time))

        visited = set()
        min_time = 0

        min_heap = [(0, k)]

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)
            min_time = curr_time

            for neighbor_node, neighbor_time in edge_list[curr_node]:
                if neighbor_node not in visited:
                    heapq.heappush(min_heap, (curr_time + neighbor_time, neighbor_node))

        return min_time if len(visited) == n else -1

        

        