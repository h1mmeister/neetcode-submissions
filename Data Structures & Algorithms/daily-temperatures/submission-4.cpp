class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        size_t n = temperatures.size();
        vector<int> result(n, 0);

        vector<int> st;
        st.reserve(n);

        for (size_t idx=0; idx < n; ++idx) {
            int curr_temp = temperatures[idx];

            while (!st.empty() && curr_temp > temperatures[st.back()]) {
                int prev_idx = st.back();
                st.pop_back();
                result[prev_idx] = idx - prev_idx;
            }
            st.push_back(idx);
        }
        return result;
    }
};
