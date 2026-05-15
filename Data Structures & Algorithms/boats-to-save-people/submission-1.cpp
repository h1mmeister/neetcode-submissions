class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int num_of_boats = 0;
        int left = 0;
        int right = people.size() - 1;

        sort(people.begin(), people.end());

        while (left <= right) {
            if ((people[left] + people[right]) <= limit) {
                left += 1;
            }
            right -= 1;
            num_of_boats += 1;
        }
        return num_of_boats;
    }
};