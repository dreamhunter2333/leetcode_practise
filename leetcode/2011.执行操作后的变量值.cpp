#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=2011 lang=cpp
 *
 * [2011] 执行操作后的变量值
 */

// @lc code=start
class Solution
{
public:
    unordered_map<string, int> map = {{"X++", 1}, {"++X", 1}, {"--X", -1}, {"X--", -1}};

    int finalValueAfterOperations(vector<string> &operations)
    {
        int res = 0;
        for (auto &&op : operations)
        {
            res += map[op];
        }
        return res;
    }
};
// @lc code=end
