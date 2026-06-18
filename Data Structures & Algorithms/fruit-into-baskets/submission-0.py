class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        type_of_fruits = {}
        max_fruits = 0

        left = 0
        for right in range(len(fruits)):
            if fruits[right] not in type_of_fruits:
                type_of_fruits[fruits[right]] = 1
            else:
                type_of_fruits[fruits[right]] += 1

            while len(type_of_fruits) > 2:
                type_of_fruits[fruits[left]] -= 1
                if type_of_fruits[fruits[left]] == 0:
                    del type_of_fruits[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

