class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;
        int left = 0;
        int right = heights.size() - 1;

        while (left < right) {
            int first_bar = heights[left];
            int second_bar = heights[right];

            int curr_max_area = min(first_bar, second_bar) * (right - left);
            max_area = max(max_area, curr_max_area);

            if (first_bar < second_bar) {
                left++;
            } else {
                right--;
            }
        }
        return max_area;
    }
};
