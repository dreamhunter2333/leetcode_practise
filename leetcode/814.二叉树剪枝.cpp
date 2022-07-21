#include <iostream>
using namespace std;
/*
 * @lc app=leetcode.cn id=814 lang=cpp
 *
 * [814] 二叉树剪枝
 */

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// @lc code=start
class Solution
{
public:
    TreeNode *pruneTree(TreeNode *root)
    {
        function<bool(TreeNode *)> f;
        f = [&](TreeNode *node) -> bool
        {
            if (node == nullptr)
                return true;
            auto left = f(node->left);
            auto right = f(node->right);
            if (node->val == 0 && left && right)
                return true;
            if (left)
                node->left = nullptr;
            if (right)
                node->right = nullptr;
            return false;
        };
        return f(root) ? nullptr : root;
    }
};
// @lc code=end
