class Solution {
private:
    std::vector<std::vector<int>> create_adj_list(int num_courses, const std::vector<std::vector<int>>& pre_reqs) {
        std::vector<std::vector<int>> adj_list(num_courses);

        for(const auto& pair : pre_reqs) {
            int course = pair[0];
            int pre_req = pair[1];

            adj_list[course].push_back(pre_req);
        }
        return adj_list;
    }

    bool has_cycle(int course, std::vector<int>& state, const std::vector<std::vector<int>>& adj_list) {
        if(state[course] == -1) {
            return true;
        }
        if (state[course] == 1) {
            return false;
        }

        state[course] = -1;

        for (int pre_req : adj_list[course]) {
            if (has_cycle(pre_req, state, adj_list)) {
                return true;
            }
        }

        state[course] = 1;
        return false;

    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<std::vector<int>> adj_list = create_adj_list(numCourses, prerequisites);
        std::vector<int> state(numCourses, 0);

        for (int course {0}; course < numCourses; ++course) {
            if (has_cycle(course, state, adj_list)) {
                return false;
            }
        }
        return true;
    }
};
