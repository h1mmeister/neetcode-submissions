class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        max_freq = 0
        freq = {}

        left = 0
        for right in range(0, len(s)):
            char = s[right]
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

            max_freq = max(max_freq, freq[char])

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result
        