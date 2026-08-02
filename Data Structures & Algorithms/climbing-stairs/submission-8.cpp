class Solution {
public:
    int climbStairs(int n) {
        unordered_map<int, int> cache;
        return climbing_stairs_helper(n, cache);
    }

private:
    int climbing_stairs_helper(int n, unordered_map<int, int>& cache) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        }

        if (cache.find(n) != cache.end()) {
            return cache[n];
        }
        cache[n] = climbing_stairs_helper(n - 1, cache) + climbing_stairs_helper (n - 2, cache);
        return cache[n];
    }
};
