class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(idx, target, curr):
            if target == 0:
                result.append(curr.copy())
                return
            
            if idx >= len(nums) or nums[idx] > target:
                return

            curr.append(nums[idx])
            dfs(idx, target - nums[idx], curr)

            curr.pop()
            dfs(idx + 1, target, curr)

        dfs(0, target, [])
        return result
        