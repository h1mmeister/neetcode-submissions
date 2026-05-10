class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t_temp, t_idx = stack.pop()
                result[t_idx] = idx - t_idx
            stack.append((temp, idx))

        return result
        