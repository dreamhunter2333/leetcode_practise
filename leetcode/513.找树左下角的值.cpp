#include <iostream>
#include <list>
using namespace std;
/*
 * @lc app=leetcode.cn id=513 lang=cpp
 *
 * [513] 找树左下角的值
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
    int findBottomLeftValue(TreeNode *root)
    {
        list<TreeNode *> nodeList;
        nodeList.push_back(root);
        TreeNode *res;
        while (!nodeList.empty())
        {
            res = nodeList.front();
            int n = nodeList.size();
            for (int i = 0; i < n; i++)
            {
                TreeNode *node = nodeList.front();
                nodeList.pop_front();
                if (node->left != nullptr)
                {
                    nodeList.push_back(node->left);
                }
                if (node->right != nullptr)
                {
                    nodeList.push_back(node->right);
                }
            }
        }
        return res->val;
    }
};
// @lc code=end
int main()
{
    TreeNode node1 = TreeNode(1);
    TreeNode node3 = TreeNode(3);
    TreeNode node2 = TreeNode(2, &node1, &node3);
    cout << Solution().findBottomLeftValue(&node2) << endl;
    return 0;
}
