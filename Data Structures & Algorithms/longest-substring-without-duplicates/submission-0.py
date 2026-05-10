class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for i in range(0, len(s)):
            visited = set()
            for j in range(i, len(s)):
                char = s[j]

                if char in visited:
                    break
                
                visited.add(char)
                result = max(result, len(visited))
                
        return result
        