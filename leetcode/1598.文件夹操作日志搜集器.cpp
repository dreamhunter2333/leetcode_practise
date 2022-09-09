#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1598 lang=cpp
 *
 * [1598] 文件夹操作日志搜集器
 */

// @lc code=start
class Solution
{
public:
    int minOperations(vector<string> &logs)
    {
        int level = 0;
        for (auto &&log_item : logs)
        {
            if (log_item == "../")
            {
                if (level > 0)
                {
                    level -= 1;
                }
            }
            else if (log_item != "./")
            {
                level += 1;
            }
        }
        return level;
    }
};
// @lc code=end
