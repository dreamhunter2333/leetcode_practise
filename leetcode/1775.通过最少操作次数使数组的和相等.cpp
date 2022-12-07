#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
/*
 * @lc app=leetcode.cn id=1775 lang=cpp
 *
 * [1775] 通过最少操作次数使数组的和相等
 */

// @lc code=start
class Solution
{
public:
    int minOperations(vector<int> &nums1, vector<int> &nums2)
    {
        int delta = accumulate(nums1.begin(), nums1.end(), 0) - accumulate(nums2.begin(), nums2.end(), 0);
        if (delta == 0)
            return 0;
        if (delta < 0)
        {
            swap(nums1, nums2);
            delta = -delta;
        }
        if (nums2.size() * 6 < nums1.size() * 1)
            return -1;
        vector<int> delta_nums;
        for (auto &&num : nums1)
            delta_nums.push_back(num - 1);
        for (auto &&num : nums2)
            delta_nums.push_back(6 - num);
        sort(delta_nums.begin(), delta_nums.end(), [](const int &a, const int &b)
             { return a > b; });

        int res = 0;
        while (delta > 0)
        {
            delta -= delta_nums[res];
            res++;
        }
        return res;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums1({1, 2, 3, 4, 5, 6});
    vector<int> nums2({1, 1, 2, 2, 2, 2});
    cout << s.minOperations(nums1, nums2) << endl;
    return 0;
}
