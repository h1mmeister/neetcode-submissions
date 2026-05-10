class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        v = set()
        left = 0

        for right in range(0, len(s)):
            char = s[right]

            while char in v:
                v.remove(s[left])
                left += 1
            
            v.add(char)

            result = max(result, right - left + 1)


        return result

        