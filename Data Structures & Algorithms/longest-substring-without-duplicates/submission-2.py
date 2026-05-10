class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        left = 0
        visited = set()

        for right in range(0, len(s)):
            char = s[right]

            while char in visited:
                visited.remove(s[left])
                left += 1

            visited.add(char)
            result = max(result, len(visited))

        return result



        