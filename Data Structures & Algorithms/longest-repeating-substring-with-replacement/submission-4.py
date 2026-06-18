class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        hash_map = {}

        left = 0
        for right in range(len(s)):
            right_char = s[right]

            if right_char not in hash_map:
                hash_map[right_char] = 1
            else:
                hash_map[right_char] += 1

            while (right - left + 1) - max(hash_map.values()) > k:
                left_char = s[left];
                hash_map[left_char] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


            
