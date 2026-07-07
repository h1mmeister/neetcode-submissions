#include <string>
#include <vector>
#include <climits>

class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return "";
        }

        // Use fixed-size stack arrays instead of heavy unordered_maps
        int required_count[128] = {0};
        int window_count[128] = {0};

        // Populate target frequencies
        int need = 0;
        for (char c : t) {
            if (required_count[c] == 0) {
                need++; // Count unique characters needed
            }
            required_count[c]++;
        }

        int have = 0;
        int min_length = INT_MAX;
        int start_idx = 0;
        int left = 0;

        // Sliding window boundary expansion
        for (int right = 0; right < s.length(); ++right) {
            char right_char = s[right];
            
            if (required_count[right_char] > 0) {
                window_count[right_char]++;
                if (window_count[right_char] == required_count[right_char]) {
                    have++;
                }
            }

            // Shrink window from the left while current window remains valid
            while (have == need) {
                int curr_length = right - left + 1;
                if (curr_length < min_length) {
                    min_length = curr_length;
                    start_idx = left;
                }

                char left_char = s[left];
                if (required_count[left_char] > 0) {
                    if (window_count[left_char] == required_count[left_char]) {
                        have--;
                    }
                    window_count[left_char]--;
                }
                left++;
            }
        }

        return (min_length == INT_MAX) ? "" : s.substr(start_idx, min_length);
    }
};