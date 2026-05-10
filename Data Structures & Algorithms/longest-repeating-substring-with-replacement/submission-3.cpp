class Solution {
public:
    int characterReplacement(string s, int k) {
        int result = 0;
        unordered_map<char, int> freq;

        int max_freq = 0;
        int left = 0;

        for (int right = 0; right < s.size(); right++){
            int ch = s[right];

            freq[ch]++;
            max_freq = max(max_freq, freq[ch]);

            while (((right - left + 1) - max_freq) > k) {
                freq[s[left]]--;
                left++;
            }

            result = max(result, right - left + 1);
        }

        return result;
        
    }
};
