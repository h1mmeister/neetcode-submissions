class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max_area = 0;

        for (int i = 0; i < heights.size() - 1; i++){
            int first_pillar = heights[i];
            for (int j = i + 1; j < heights.size(); j++){
                int second_pillar = heights[j];

                int curr_area = min(first_pillar, second_pillar) * (j - i);
                max_area = max(max_area, curr_area);
            }
        }

        return max_area;
    }
};
