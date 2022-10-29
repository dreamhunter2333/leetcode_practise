#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=1773 lang=cpp
 *
 * [1773] 统计匹配检索规则的物品数量
 */

// @lc code=start
class Solution
{
public:
    int countMatches(vector<vector<string>> &items, string ruleKey, string ruleValue)
    {
        int index = ruleKey == "type" ? 0 : (ruleKey == "color" ? 1 : 2);
        int res = 0;
        for (auto &&item : items)
        {
            if (item[index] == ruleValue)
                res++;
        }
        return res;
    }
};
// @lc code=end
