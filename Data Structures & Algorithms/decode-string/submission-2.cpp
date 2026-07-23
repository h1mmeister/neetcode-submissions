class Solution {
public:
    string decodeString(string s) {
        string curr_str = "";
        int curr_count = 0;

        vector<string> stack_str;
        vector<int> stack_int;

        for (char ch : s) {
            if (ch == '[') {
                stack_str.push_back(curr_str);
                stack_int.push_back(curr_count);
                curr_count = 0;
                curr_str = "";
            } else if (ch == ']') {
                int prev_count = stack_int.back();
                stack_int.pop_back();
                string prev_str = stack_str.back();
                stack_str.pop_back();
                
                string temp = "";
                for (int i = 0; i < prev_count; ++i) {
                    temp += curr_str;
                }
                curr_str = prev_str + temp;

            } else if (isdigit(ch)) {
                curr_count = 10 * curr_count + (ch - '0');
            } else {
                curr_str += ch;
            }
        }
        return curr_str;
    }
};