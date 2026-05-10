class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        for i in range(0, len(numbers) - 1):
            first_num = numbers[i]
            for j in range(i + 1, len(numbers)):
                second_num = numbers[j]

                total = first_num + second_num
                if total == target:
                    result = [i + 1, j + 1]

        return result
        