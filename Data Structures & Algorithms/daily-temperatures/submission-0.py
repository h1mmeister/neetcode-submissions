class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            curr_temp = temperatures[i]
            for j in range(i + 1, len(temperatures)):
                next_temp = temperatures[j]

                if next_temp > curr_temp:
                    result[i] = j - i
                    break

        return result
        