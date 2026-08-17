class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& words) {
        unordered_map<string, vector<string>> hash_map;
        vector<vector<string>> result;

        for (const string& word : words) {
            string key = word;
            sort(key.begin(), key.end());
            hash_map[key].push_back(word);
        }

        result.reserve(hash_map.size());
        
        for (auto& [_, value] : hash_map) {
            result.push_back(std::move(value));
        }

        return result;
    }
};
