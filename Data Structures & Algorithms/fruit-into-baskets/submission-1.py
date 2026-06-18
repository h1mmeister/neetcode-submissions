from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = Counter()

        left = 0
        for right in range(len(fruits)):
            basket[fruits[right]] += 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

        return right - left + 1

        