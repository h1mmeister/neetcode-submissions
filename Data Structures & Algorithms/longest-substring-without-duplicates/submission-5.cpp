class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int result = 0;
        int left = 0;

        unordered_map<char, int> visited;

        for (int right = 0; right < s.size(); right++){
            char ch = s[right];

            if (visited.find(ch) != visited.end()) {
                left = max(left, visited[ch] + 1);
            }
            visited[ch] = right;
            result = max(result, (right - left + 1));
        }
        return result;
    }
};
