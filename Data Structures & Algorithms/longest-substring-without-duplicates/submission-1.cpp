class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int result = 0;

        for (int i = 0; i < s.size(); i++){
            unordered_set<char> visited;
            for (int j = i; j < s.size(); j++){
                char ch = s[j];

                if (visited.find(ch) != visited.end()) {
                    break;
                }

                visited.insert(ch);
                result = max(result, (int)visited.size());
            }
        }
        return result;
    }
};
