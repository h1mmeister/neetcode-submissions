class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(num_courses)]

        for c1, c2 in prerequisites:
            adj_list[c1].append(c2)

        state = [0] * num_courses

        # 0 -> not checked
        # 1 -> completed
        # -1 -> in progress

        def has_cycle(course):
            if state[course] == 1:
                return False
            
            if state[course] == -1:
                return True

            state[course] = -1

            for neighbor in adj_list[course]:
                if has_cycle(neighbor):
                    return True

            state[course] = 1
            return False

        for course in range(0, num_courses):
            if has_cycle(course):
                return False

        return True

        