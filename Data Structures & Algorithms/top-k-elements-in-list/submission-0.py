class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        sorted_hash_map = sorted(hash_map.items(), key = lambda x :x[1], reverse = True)

        for key, value in sorted_hash_map:
            if len(result) == k:
                break
            else:
                result.append(key)

        return result

        