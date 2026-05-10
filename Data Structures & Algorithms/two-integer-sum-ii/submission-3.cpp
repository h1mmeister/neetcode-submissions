class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result;

        for (int i = 0; i < numbers.size() - 1; i++){
            int first_num = numbers[i];
            for (int j = i + 1; j < numbers.size(); j++) {
                int second_num = numbers[j];
                int total = first_num +  second_num;

                if (target == total) {
                    result = {i + 1, j + 1};
                }
            }
        }

        return result;
        
    }
};
