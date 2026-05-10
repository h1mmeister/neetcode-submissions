class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        longest_substr_length = float('-infinity')
        freq_map = {}

        left = 0
        for right in range(0, len(s)):
            right_char = s[right]

            if right_char not in freq_map:
                freq_map[right_char] = 1
            else:
                freq_map[right_char] += 1

            while len(freq_map) > 2:
                left_char = s[left]
                freq_map[left_char] -= 1

                if freq_map[left_char] == 0:
                    del freq_map[left_char]
                left += 1
            
            curr_substr_length = right - left + 1
            longest_substr_length = max(longest_substr_length, curr_substr_length)

        return longest_substr_length


            
        