class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)])
        result = []
        heap = []
        time = 0
        i = 0

        while i < len(sorted_tasks) or heap:
            while i < len(sorted_tasks) and sorted_tasks[i][0] <= time:
                _, process, idx = sorted_tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            if not heap:
                time = sorted_tasks[i][0]
                continue
            
            process, idx = heapq.heappop(heap)
            time += process
            result.append(idx)

        return result
            
            
        