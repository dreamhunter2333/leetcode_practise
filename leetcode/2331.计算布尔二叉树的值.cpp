/*
 * @lc app=leetcode.cn id=2331 lang=cpp
 *
 * [2331] 计算布尔二叉树的值
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
    bool evaluateTree(TreeNode *node)
    {
        if (!node->left || !node->right)
        {
            return node->val == 1;
        }
        if (node->val == 2)
        {
            return evaluateTree(node->left) || evaluateTree(node->right);
        }
        return evaluateTree(node->left) && evaluateTree(node->right);
    }
};
// @lc code=end
