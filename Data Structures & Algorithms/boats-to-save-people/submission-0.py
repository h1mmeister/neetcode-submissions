class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        num_of_boats = 0

        left = 0
        right = len(people) - 1

        people.sort()

        while left <= right:
            if (people[left] + people[right]) <= limit:
                left += 1

            right -= 1
            num_of_boats += 1

        return num_of_boats
        