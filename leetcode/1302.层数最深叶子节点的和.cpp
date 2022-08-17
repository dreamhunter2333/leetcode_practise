#include <iostream>
#include <queue>
using namespace std;
/*
 * @lc app=leetcode.cn id=1302 lang=cpp
 *
 * [1302] 层数最深叶子节点的和
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
    int deepestLeavesSum(TreeNode *root)
    {
        queue<TreeNode *> qu;
        qu.emplace(root);
        int res;
        while (qu.size() > 0)
        {
            res = 0;
            int count = qu.size();
            for (size_t i = 0; i < count; i++)
            {
                auto node = qu.front();
                qu.pop();
                res += node->val;
                if (node->left != nullptr)
                {
                    qu.emplace(node->left);
                }
                if (node->right != nullptr)
                {
                    qu.emplace(node->right);
                }
            }
        }
        return res;
    }
};
// @lc code=end
