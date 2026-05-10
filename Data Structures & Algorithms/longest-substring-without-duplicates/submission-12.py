class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_susbstr_length = 0
        chars_set = set()

        left = 0
        for right in range(0, len(s)):
            right_char = s[right]

            while right_char in chars_set:
                left_char = s[left]
                chars_set.remove(left_char)
                left += 1

            chars_set.add(right_char)
            longest_susbstr_length = max(longest_susbstr_length, right - left + 1)

        return longest_susbstr_length