class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substr_length = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substr = s[i : j + 1]
                if len(substr) > longest_substr_length and not self.check_repeating_chars(substr):
                    longest_substr_length = len(substr)

        return longest_substr_length

    def check_repeating_chars(self, s):
        chars_set = set()

        for char in s:
            if char not in chars_set:
                chars_set.add(char)
            else:
                return True

        return False
        