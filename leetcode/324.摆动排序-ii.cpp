#include <vector>
#include <algorithm>
using namespace std;
/*
 * @lc app=leetcode.cn id=324 lang=cpp
 *
 * [324] 摆动排序 II
 */

// @lc code=start
class Solution
{
public:
    void wiggleSort(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> arr = nums;
        sort(arr.begin(), arr.end());
        int x = (n + 1) / 2;
        int j = x - 1, k = n - 1;
        for (size_t i = 0; i < n; i += 2)
        {
            nums[i] = arr[j];
            if (i + 1 < n)
                nums[i + 1] = arr[k];
            j -= 1;
            k -= 1;
        }
    }
};
// @lc code=end
