#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;
/*
 * @lc app=leetcode.cn id=1817 lang=cpp
 *
 * [1817] 查找用户活跃分钟数
 */

// @lc code=start
class Solution
{
public:
    vector<int> findingUsersActiveMinutes(vector<vector<int>> &logs, int k)
    {
        vector<int> res(k, 0);
        unordered_map<int, unordered_set<int>> cache_map;
        for (auto &&log : logs)
        {
            cache_map[log[0]].emplace(log[1]);
        }
        for (auto &&i : cache_map)
        {
            res[i.second.size() - 1] += 1;
        }
        return res;
    }
};
// @lc code=end
