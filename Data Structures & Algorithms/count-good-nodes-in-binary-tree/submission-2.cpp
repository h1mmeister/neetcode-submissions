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
        int good_nodes = 0;

        if (root == nullptr) {
            return good_nodes;
        }

        using node_state = pair<TreeNode*, int>;

        queue<node_state> q;
        q.push({root, INT_MIN});

        while (!q.empty()) {
            TreeNode* node = q.front().first;
            int max_value = q.front().second;

            q.pop();

            if (node->val >= max_value) {
                good_nodes++;
            }

            int new_max_value = max(max_value, node->val);

            if (node->left) {
                q.push({node->left, new_max_value});
            }
            if (node->right) {
                q.push({node->right, new_max_value});
            }
        }

        return good_nodes;
        
    }
};
