class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_susbstr_length = 0

        for i in range(0, len(s)):
            chars_set = set()
            for j in range(i, len(s)):
                if s[j] in chars_set:
                    break
                chars_set.add(s[j])

            longest_susbstr_length = max(longest_susbstr_length, len(chars_set))

        return longest_susbstr_length
        