class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int result = 0;

        int left = 0;
        unordered_set<char> visited;

        for (int right = 0; right < s.size(); right++) {
            char ch = s[right];

            while (visited.find(ch) != visited.end()) {
                visited.erase(s[left]);
                left++;
            }

            visited.insert(ch);
            result = max(result, (int)visited.size());
        }
        return result;
    }
};
