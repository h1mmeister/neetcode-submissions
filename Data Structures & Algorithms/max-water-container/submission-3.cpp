class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;

        int left = 0;
        int right = heights.size() - 1;

        while (left < right){
            int first_pillar = heights[left];
            int second_pillar = heights[right];

            int min_pillar = min(first_pillar, second_pillar);
            int curr_area = min_pillar * (right - left);
            max_area = max(max_area, curr_area);

            if (first_pillar < second_pillar) {
                left++;
            } else {
                right--;
            }

        }
    return max_area;
    }
};
