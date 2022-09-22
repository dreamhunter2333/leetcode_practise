#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=1640 lang=cpp
 *
 * [1640] 能否连接形成数组
 */

// @lc code=start
class Solution
{
public:
    bool canFormArray(vector<int> &arr, vector<vector<int>> &pieces)
    {
        unordered_map<int, int> arr_map;
        for (size_t i = 0; i < arr.size(); i++)
            arr_map[arr[i]] = i;
        for (auto &&piece : pieces)
        {
            int pre_index = -1;
            for (auto &&num : piece)
            {
                if (!arr_map.count(num) || (pre_index != -1 && arr_map[num] - pre_index != 1))
                    return false;
                pre_index = arr_map[num];
            }
        }
        return true;
    }
};
// @lc code=end
