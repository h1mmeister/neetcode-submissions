class Solution {
public:
    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        unordered_map<string, unordered_set<string>> graph;
        unordered_map<string, string> email_to_name;

        for (auto& account : accounts) {
            string& name = account[0];

            for (int i = 1; i < account.size(); ++i) {
                graph[account[1]].insert(account[i]);
                graph[account[i]].insert(account[1]);
                email_to_name[account[i]] = name;
            }
        }

        unordered_set<string> visited;
        vector<vector<string>> result;

        for (auto& [email, _] : graph) {
            if (visited.count(email)) continue;
            visited.insert(email);
            vector<string> component;
            stack<string> st;
            st.push(email);

            while (!st.empty()) {
                string curr_email = st.top();
                st.pop();
                component.push_back(curr_email);

                for (auto& neighbor : graph[curr_email]) {
                    if (visited.count(neighbor)) continue;
                    visited.insert(neighbor);
                    st.push(neighbor);
                }
            }
            sort(component.begin(), component.end());
            component.insert(component.begin(), email_to_name[email]);
            result.push_back(component);
        }
        return result;
    }
};