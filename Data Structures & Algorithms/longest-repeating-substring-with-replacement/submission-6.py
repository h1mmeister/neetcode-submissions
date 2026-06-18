class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        longest_substring = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            hash_map[s[right]] = hash_map.get(s[right], 0) + 1
            max_freq = max(max_freq, hash_map[s[right]])
            
            while (right - left + 1) - max_freq > k:
                hash_map[s[left]] -= 1
                left += 1
            
            longest_substring = max(longest_substring,  right - left + 1)
            
        return longest_substring