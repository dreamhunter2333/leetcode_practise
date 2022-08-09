#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1413 lang=cpp
 *
 * [1413] 逐步求和得到正数的最小值
 */

// @lc code=start
class Solution
{
public:
    int minStartValue(vector<int> &nums)
    {
        int minNum = 0, sumNum = 0;
        for (auto &&num : nums)
        {
            sumNum += num;
            minNum = min(minNum, sumNum);
        }
        return 1 - minNum;
    }
};
// @lc code=end
