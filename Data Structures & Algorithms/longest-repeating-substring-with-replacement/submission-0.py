class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        freq = {}

        left = 0
        for right in range(0, len(s)):
            char = s[right]
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result
        