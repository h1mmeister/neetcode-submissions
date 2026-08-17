
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& words) {
        unordered_map<string, vector<string>> hash_map;

        for (const string& word : words) {
            array<int, 26> count = {}; 
            for (char c : word) {
                count[c - 'a']++;
            }
           
            string key(count.begin(), count.end());
            hash_map[key].push_back(word);
        }

        vector<vector<string>> result;
        result.reserve(hash_map.size());
        for (auto& [key, group] : hash_map) {
            result.push_back(move(group));
        }
        return result;
    }
};
