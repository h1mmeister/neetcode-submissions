class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result = {};

        unordered_map<int, int> freq;
        for (int i = 0; i < numbers.size(); i++) {
            int first_num = numbers[i];

            int second_num = target - first_num;

            if (freq.count(second_num)){
                result = {freq[second_num], i + 1};
            }

            freq[first_num] = i + 1;
        }

        return result;

    }
};
