#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=2303 lang=cpp
 *
 * [2303] 计算应缴税款总额
 */

// @lc code=start
class Solution
{
public:
    double calculateTax(vector<vector<int>> &brackets, int income)
    {
        double res = 0;
        int pre_upper = 0;
        for (auto &&bracket : brackets)
        {
            int upper = bracket[0];
            int percent = bracket[1];
            if (income < upper)
            {
                res += (income - pre_upper) * percent;
                break;
            }
            res += (upper - pre_upper) * percent;
            pre_upper = upper;
        }
        return res / 100;
    }
};
// @lc code=end
