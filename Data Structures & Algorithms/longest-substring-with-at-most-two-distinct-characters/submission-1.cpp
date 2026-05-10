class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int longest_substr_length = INT_MIN;
        unordered_map<char, int> freq_map;

        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            char right_char = s[right];

            freq_map[right_char]++;

            while (freq_map.size() > 2) {
                char left_char = s[left];
                freq_map[left_char]--;

                if (freq_map[left_char] == 0) {
                    freq_map.erase(left_char);
                }
                
                left += 1;
            }

            int curr_substr_length = right - left + 1;
            longest_substr_length = max(longest_substr_length, curr_substr_length);

        }
        return longest_substr_length;
    }
};