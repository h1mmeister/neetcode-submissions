class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []

        hash_map = defaultdict(list)

        for word in words:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            hash_map[tuple(count)].append(word)

        return list(hash_map.values())
        