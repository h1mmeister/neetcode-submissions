class Solution {
public:
    int characterReplacement(string s, int k) {
        int result = 0;

        std::unordered_map<char, int> hash_map;
        int left = 0;
        int right = 0;
        int max_freq = 0;

        for (right = 0; right < s.length(); ++right) {
            hash_map[s[right]]++;

            max_freq = max(max_freq, hash_map[s[right]]);

            while (((right - left + 1) - (max_freq)) > k ) {
                hash_map[s[left]]--;
                left++;
            }

            result = max(result, right - left + 1);
        }
        return result;
    }
};
