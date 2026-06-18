class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hash_map = {}

        left = 0
        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1

            while (right - left + 1) - max(hash_map.values()) > k:
                hash_map[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
