#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1441 lang=cpp
 *
 * [1441] 用栈操作构建数组
 */

// @lc code=start
class Solution
{
public:
    vector<string> buildArray(vector<int> &target, int n)
    {
        vector<string> res;
        int pre = 0;
        for (auto &&i : target)
        {
            if (i - pre > 1)
            {
                for (size_t j = 0; j < i - pre - 1; j++)
                {
                    res.push_back("Push");
                    res.push_back("Pop");
                }
            }
            res.push_back("Push");
            pre = i;
        }
        return res;
    }
};
// @lc code=end
