class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        adj_list = [[] for _ in range(num_courses)]
        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)


        state = [0] * num_courses

        def has_cycle(course):
            if state[course] == 1:
                return False
            
            if state[course] == -1:
                return True

            state[course] = -1

            for neighbors in adj_list[course]:
                if has_cycle(neighbors):
                    return True
            
            state[course] = 1
            result.append(course)
            return False


        for course in range(num_courses):
            if has_cycle(course):
                return []

        return result
        