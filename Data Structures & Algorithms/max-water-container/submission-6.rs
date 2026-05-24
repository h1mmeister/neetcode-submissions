impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut max_area = 0;

        let mut left = 0;
        let mut right = heights.len() - 1;

        while left < right {
            let first_bar = heights[left];
            let second_bar = heights[right];

            let curr_max_area = first_bar.min(second_bar) * (right - left) as i32;
            max_area = max_area.max(curr_max_area);

            if first_bar < second_bar {
                left += 1;
            } else {
                right -= 1
            }
        }
        return max_area;
    }
}
