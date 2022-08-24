#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=1460 lang=cpp
 *
 * [1460] 通过翻转子数组使两个数组相等
 */

// @lc code=start
class Solution
{
public:
    bool canBeEqual(vector<int> &target, vector<int> &arr)
    {
        unordered_map<int, int> count1;
        for (auto &&t : target)
        {
            count1[t]++;
        }
        unordered_map<int, int> count2;
        for (auto &&a : arr)
        {
            count2[a]++;
        }
        return count1 == count2;
    }
};
// @lc code=end
