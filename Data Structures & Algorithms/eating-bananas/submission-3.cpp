class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());
        int result = right;

        while (left <= right) {
            int speed = left + (right - left) / 2;

            long long total_time = 0;
            for (const auto& pile : piles) {
                total_time += (pile + speed - 1) /speed;
            }

            if (total_time <= h) {
                result = speed;
                right = speed - 1;
            } else {
                left = speed + 1;
            }
        }
        return result;
    }
};
