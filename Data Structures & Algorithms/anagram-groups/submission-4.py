class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []

        hash_map = {}

        for word in words:
            count = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1

            key = tuple(count)
            if key not in hash_map:
                hash_map[key] = [word]
            else:
                hash_map[key].append(word)

        return list(hash_map.values())
        