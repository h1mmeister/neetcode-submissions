class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = {}
        max_heap = []
        result = []
        prev = None

        for ch in s:
            if ch not in freq_map:
                freq_map[ch] = 1
            else:
                freq_map[ch] += 1

        for k, v in freq_map.items():
            max_heap.append((-v, k))

        heapq.heapify(max_heap)

        while max_heap or prev:

            if prev and len(max_heap) == 0:
                return ""

            count, ch = heapq.heappop(max_heap)
            result.append(ch)
            count += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if count != 0:
                prev = (count, ch)

        return "".join(result)



