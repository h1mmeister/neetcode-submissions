class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        curr_num_of_passengers = 0
        min_heap = []

        for num_of_passengers, start, end in trips:

            while min_heap and min_heap[0][0] <= start:
                curr_num_of_passengers -= heapq.heappop(min_heap)[1]

            curr_num_of_passengers += num_of_passengers
            if curr_num_of_passengers > capacity:
                return False

            heapq.heappush(min_heap, [end, num_of_passengers])

        return True

        