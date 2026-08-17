class Solution:
    def findMedianSortedArrays(self, array_one: List[int], array_two: List[int]) -> float:
        median_idx = (len(array_one) + len(array_two) - 1) // 2

        idx1 = 0
        idx2 = 0

        while idx1 + idx2 < median_idx:
            if idx1 == len(array_one):
                idx2 += 1
            elif idx2 == len(array_two):
                idx1 += 1
            elif array_one[idx1] < array_two[idx2]:
                idx1 += 1
            else:
                idx2 += 1

        if (len(array_one) + len(array_two)) % 2 == 0:
            both_values_array_one = idx2 >= len(array_two) or (idx1 + 1 < len(array_one) and array_two[idx2] > array_one[idx1 + 1])
            both_values_array_two = idx1 >= len(array_one) or (idx2 + 1 < len(array_two) and array_one[idx1] > array_two[idx2 + 1])

            value_one = array_one[idx1 + 1] if both_values_array_one else array_two[idx2]
            value_two = array_two[idx2 + 1] if both_values_array_two else array_one[idx1]
            return (value_one +  value_two) / 2
        else:
            value_one = array_one[idx1] if idx1 < len(array_one) else float("inf")
            value_two = array_two[idx2] if idx2 < len(array_two) else float("inf")
            return min(value_one, value_two)
        