class MedianFinder:

    def __init__(self):
        self.max_heap_left = []
        self.min_heap_right = []
        self.median = None

    def update_mean(self):
        left_size = len(self.max_heap_left)
        right_size = len(self.min_heap_right)

        if left_size == right_size:
            self.median = (-1 * self.max_heap_left[0] + self.min_heap_right[0]) / 2
            return self.median
        elif left_size > right_size:
            self.median = -1 * self.max_heap_left[0]
            return self.median
        else:
            self.median = self.min_heap_right[0]
            return self.median


    def addNum(self, num: int) -> None:
        if not self.max_heap_left or num <= -1 * self.max_heap_left[0]:
            heapq.heappush(self.max_heap_left, -1 * num)
        else:
            heapq.heappush(self.min_heap_right, num)

        left_size = len(self.max_heap_left)
        right_size = len(self.min_heap_right)

        if abs(left_size - right_size) > 1:
            if left_size > right_size:
                elem = heapq.heappop(self.max_heap_left)
                heapq.heappush(self.min_heap_right, -1 * elem)
            else:
                elem = heapq.heappop(self.min_heap_right)
                heapq.heappush(self.max_heap_left, -1 * elem)

        self.update_mean()

    def findMedian(self) -> float:
        return self.median
        
        