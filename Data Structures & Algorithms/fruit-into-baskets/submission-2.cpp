class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        std::unordered_map<int, int> basket;
        int left = 0;
        int right = 0;

        for (right = 0; right < fruits.size(); ++right) {
            basket[fruits[right]]++;

            if (basket.size() > 2) {
                basket[fruits[left]]--;
                if (basket[fruits[left]] == 0) {
                    basket.erase(fruits[left]);
                }
                left++;
            }
        }
        
        return (right - left);
    }
};