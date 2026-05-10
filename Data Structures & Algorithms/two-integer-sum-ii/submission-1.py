class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        freq = {}

        for i in range(0, len(numbers)):
            first_num = numbers[i]
            second_num = target - first_num

            if second_num in freq:
                result = [freq[second_num], i + 1]
                return result 

            freq[first_num] = i + 1

        return result


        