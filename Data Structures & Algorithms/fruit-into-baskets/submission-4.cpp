class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int max_num = *max_element(fruits.begin(), fruits.end());
        std::vector<int> basket(max_num + 1, 0);
        int distinct_fruits = 0;
        int left = 0;
        int right = 0;

        for (right = 0; right < fruits.size(); ++right) {
            if (basket[fruits[right]] == 0) {
                distinct_fruits++;
            }
            basket[fruits[right]]++;

            if (distinct_fruits > 2) {
                basket[fruits[left]]--;
                if (basket[fruits[left]] == 0) {
                    distinct_fruits--;
                }
                left++;
            }
        }
        return right - left;
    }
};