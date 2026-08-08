class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def dfs(idx):
            if idx == len(s):
                return True

            if idx in cache:
                return cache[idx]

            for word in wordDict:
                if idx + len(word) <= len(s) and s[idx : idx + len(word)] == word:
                    if dfs(idx + len(word)):
                        cache[idx] = True
                        return True
            cache[idx] = False
            return cache[idx]
        return dfs(0)
        