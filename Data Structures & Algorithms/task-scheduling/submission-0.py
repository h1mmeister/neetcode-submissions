class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map = {}
        for task in tasks:
            if task not in hash_map:
                hash_map[task] = 1
            else:
                hash_map[task] += 1

        heap = [-count for task, count in hash_map.items()]
        heapq.heapify(heap)

        queue = collections.deque()

        time = 0
        while heap or queue:
            time += 1
            if heap:
                curr_count = heapq.heappop(heap)

                new_count = 1 + curr_count
                if new_count < 0:
                    queue.append([new_count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time

        