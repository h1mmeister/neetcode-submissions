class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_subset = []

        def dfs(idx):
            if idx >= len(nums):
                result.append(curr_subset.copy())
                return

            curr_subset.append(nums[idx])
            dfs(idx + 1)
            curr_subset.pop()
            dfs(idx + 1)


        dfs(0)
        return result
        