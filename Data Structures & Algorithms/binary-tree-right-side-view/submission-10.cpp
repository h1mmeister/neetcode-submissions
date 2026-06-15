/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    std::vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};

        std::vector<int> result;
        std::queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            result.push_back(q.back()->val);
            
            auto level_size = q.size(); 

            for (size_t i{0}; i < level_size; ++i) {
                TreeNode* node = q.front();
                q.pop();

                if (node->left)  q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        return result;  
    }
};
