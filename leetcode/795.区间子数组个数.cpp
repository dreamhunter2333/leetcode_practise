#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=795 lang=cpp
 *
 * [795] 区间子数组个数
 */

// @lc code=start
class Solution
{
public:
    int numSubarrayBoundedMax(vector<int> &nums, int left, int right)
    {
        int res = 0;
        int pre_count = 0;
        int min_count = 0;
        for (auto &&num : nums)
        {
            if (num < left)
            {
                min_count++;
                res += pre_count;
            }
            else if (left <= num && num <= right)
            {
                res++;
                res += (pre_count + min_count);
                pre_count += (1 + min_count);
                min_count = 0;
            }
            else
            {
                min_count = 0;
                pre_count = 0;
            }
        }
        return res;
    }
};
// @lc code=end
