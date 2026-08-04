#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead(deadends.begin(), deadends.end());
        if (dead.count("0000")) return -1;
        if (target == "0000") return 0;
        
        unordered_set<string> begin_set{"0000"};
        unordered_set<string> end_set{target};
        int turns = 0;
        
        while (!begin_set.empty() && !end_set.empty()) {
            // Always expand the smaller frontier
            if (begin_set.size() > end_set.size()) {
                swap(begin_set, end_set);
            }
            
            unordered_set<string> next_set;
            for (string lock : begin_set) {
                // Frontiers intersect
                if (end_set.count(lock)) return turns;
                
                // Skip if visited/deadend
                if (dead.count(lock)) continue;
                
                // Mark as visited
                dead.insert(lock);
                
                // Generate children
                for (int i = 0; i < 4; i++) {
                    char c = lock[i];
                    
                    // Roll wheel up
                    lock[i] = (c == '9') ? '0' : c + 1;
                    if (!dead.count(lock)) next_set.insert(lock);
                    
                    // Roll wheel down
                    lock[i] = (c == '0') ? '9' : c - 1;
                    if (!dead.count(lock)) next_set.insert(lock);
                    
                    // Backtrack to the original lock string
                    lock[i] = c; 
                }
            }
            begin_set = next_set;
            turns++;
        }
        
        return -1;
    }
};