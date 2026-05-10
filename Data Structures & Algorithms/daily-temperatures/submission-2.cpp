class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(), 0);
        stack<pair<int, int>> stack;

        for (int idx = 0; idx < temperatures.size(); idx++) {
            int curr_temp = temperatures[idx];

            while (!stack.empty() && curr_temp > stack.top().first) {
                auto pair = stack.top();
                stack.pop();
                result[pair.second] = idx - pair.second;
            }


            stack.push({curr_temp, idx});
        }
        return result;
    }
};
