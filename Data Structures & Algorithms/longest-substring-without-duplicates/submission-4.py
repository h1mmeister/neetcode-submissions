class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        left = 0
        visited = {}

        for right in range(0, len(s)):
            char = s[right]

            if char in visited:
                left = max(left, visited[char] + 1)
            
            visited[char] = right
            result = max(result, (right - left + 1))

        return result






        