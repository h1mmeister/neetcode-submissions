class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_susbstr_length = 0
        hash_map = {}

        left = 0
        for right in range(0, len(s)):
            right_char = s[right]

            if right_char not in hash_map:
                hash_map[right_char] = 1
            else:
                hash_map[right_char] += 1

            while hash_map[right_char] > 1:
                left_char = s[left]
                hash_map[left_char] -= 1
                left += 1

            longest_susbstr_length = max(longest_susbstr_length, right - left + 1)

        return longest_susbstr_length
        