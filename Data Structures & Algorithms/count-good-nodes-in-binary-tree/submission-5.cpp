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
    int goodNodes(TreeNode* root) {
        if (!root) return 0;
        return good_nodes_helper(root, root->val);   
    }

private:
    int good_nodes_helper(TreeNode* node, int max_value) {
        if (!node) return 0;

        int is_good_node = node->val >= max_value ? 1 : 0;
        max_value = max(max_value, node->val);

        int left = good_nodes_helper(node->left, max_value);
        int right = good_nodes_helper(node->right, max_value);

        return is_good_node + left + right;
    }
};
