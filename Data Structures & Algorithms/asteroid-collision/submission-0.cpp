class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stack;
        for (const auto& curr_asteroid : asteroids) {
            bool destroyed = false;

            while (!stack.empty() && curr_asteroid < 0 && stack.back() > 0) {
                if (abs(curr_asteroid) == stack.back()) {
                    stack.pop_back();
                    destroyed = true;
                    break;
                } else if (abs(curr_asteroid) > stack.back()) {
                    stack.pop_back();
                    continue;
                } else {
                    destroyed = true;
                    break;
                }

            }

            if (!destroyed) {
                stack.push_back(curr_asteroid);
            }
        }
        return stack;
    }
};