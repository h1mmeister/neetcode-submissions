class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for i in range(0, len(s)):
            v = set()
            for j in range(i, len(s)):
                if s[j] in v:
                    break
                v.add(s[j])
                result = max(result, len(v))

        return result

        