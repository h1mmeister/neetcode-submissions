class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            int curr_sum = numbers[left] + numbers[right];

            if (target == curr_sum) {
                return {left + 1, right + 1};
            } else if (target < curr_sum) {
                right--;
            } else {
                left++;
            }
        }
        
        return {};
    }
};
