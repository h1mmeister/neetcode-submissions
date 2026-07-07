from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ''
        
        required_count = Counter(t)
        need = len(required_count)
        have = 0

        freq_count = Counter()
        start = 0

        min_length = float('inf')
        left = 0

        for right, char in enumerate(s):
            if char in required_count:
                freq_count[char] += 1
                if required_count[char] == freq_count[char]:
                    have += 1
                

            while have == need:
                curr_length = right - left + 1
                if min_length > curr_length:
                    min_length = curr_length
                    start = left


                left_char = s[left]
                if left_char in required_count:
                    if required_count[left_char] == freq_count[left_char]:
                        have -= 1
                    freq_count[left_char] -= 1
                left += 1

        return '' if min_length == float('inf') else s[start : start + min_length]


