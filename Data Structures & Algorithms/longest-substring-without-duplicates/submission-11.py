class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_susbstr_length = 0
        hash_map = {}

        left = 0
        for right in range(0, len(s)):
            right_char = s[right]

            if right_char not in hash_map:
                longest_susbstr_length = max(longest_susbstr_length, right - left + 1)
            else:
                if left > hash_map[right_char]:
                    longest_susbstr_length = max(longest_susbstr_length, right - left + 1)
                else:
                    left = hash_map[right_char] + 1
                    longest_susbstr_length = max(longest_susbstr_length, right - left + 1)

            hash_map[right_char] = right

        return longest_susbstr_length
        