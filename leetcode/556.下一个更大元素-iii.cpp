#include <algorithm>
#include <string>
using namespace std;
/*
 * @lc app=leetcode.cn id=556 lang=cpp
 *
 * [556] 下一个更大元素 III
 */

// @lc code=start
class Solution
{
public:
    int nextGreaterElement(int n)
    {
        auto nums = to_string(n);
        for (size_t i = nums.size() - 1; i > 0; i--)
        {
            if (nums[i] <= nums[i - 1])
                continue;
            int max_i = i;
            for (size_t j = i + 1; j < nums.size(); j++)
            {
                if (nums[j] > nums[i - 1])
                    max_i = j;
            }
            swap(nums[i - 1], nums[max_i]);
            reverse(nums.begin() + i, nums.end());
            long ans = stol(nums);
            return ans > INT_MAX ? -1 : ans;
        }
        return -1;
    }
};
// @lc code=end
