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
    bool hasPathSum(TreeNode* root, int target_sum) {
        if (root == nullptr) {
            return false;
        }

        if (root->left == nullptr && root->right == nullptr && abs(target_sum - root->val) == 0) {
            return true;
        }

        bool left_subtree = hasPathSum(root->left, target_sum - root->val);
        bool right_subtree = hasPathSum(root->right, target_sum - root->val);

        return left_subtree || right_subtree;

        
    }
};