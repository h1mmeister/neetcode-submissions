from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for source, target, time in times:
            adj_list[source].append((target, time))

        time_map = {}
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in time_map:
                continue

            time_map[node] = time

            if len(time_map) == n:
                break

            for neighbor_node, neighbor_time in adj_list[node]:
                if neighbor_node not in time_map:
                    heapq.heappush(min_heap, (time + neighbor_time, neighbor_node))

        return -1 if len(time_map) != n else max(time_map.values())

            


        