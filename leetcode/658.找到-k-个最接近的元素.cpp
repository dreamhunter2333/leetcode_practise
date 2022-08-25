#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
 * @lc app=leetcode.cn id=658 lang=cpp
 *
 * [658] 找到 K 个最接近的元素
 */

// @lc code=start
class Solution
{
public:
    vector<int> findClosestElements(vector<int> &arr, int k, int x)
    {
        sort(arr.begin(), arr.end(), [x](const int &a, const int &b)
             {
                if (abs(a - x) == abs(b - x)) return a < b;
                return abs(a - x) < abs(b - x); });
        vector<int> res;
        for (size_t i = 0; i < k; i++)
        {
            res.push_back(arr[i]);
        }
        sort(res.begin(), res.end());
        return res;
    }
};
// @lc code=end
