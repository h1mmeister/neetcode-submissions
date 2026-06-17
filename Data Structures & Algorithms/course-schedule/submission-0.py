class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(num_courses)]
        for course, prereqs in prerequisites:
            adj_list[course].append(prereqs)

        state = [0] * num_courses

        def has_cycle(course):
            if state[course] == -1:
                return True
            if state[course] == 1:
                return False 

            state[course] = -1

            for prereqs in adj_list[course]:
                if has_cycle(prereqs):
                    return True

            state[course] = 1
            return False

        for course in range(num_courses):
            if has_cycle(course):
                return False

        return True
        