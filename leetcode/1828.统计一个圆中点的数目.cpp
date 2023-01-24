#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1828 lang=cpp
 *
 * [1828] 统计一个圆中点的数目
 */

// @lc code=start
class Solution
{
public:
    vector<int> countPoints(vector<vector<int>> &points, vector<vector<int>> &queries)
    {
        vector<int> res;
        for (auto &&query : queries)
        {
            int cur_count = 0;
            for (auto &&point : points)
            {
                if ((point[0] - query[0]) * (point[0] - query[0]) + (point[1] - query[1]) * (point[1] - query[1]) <= query[2] * query[2])
                {
                    cur_count++;
                }
            }
            res.push_back(cur_count);
        }
        return res;
    }
};
// @lc code=end
