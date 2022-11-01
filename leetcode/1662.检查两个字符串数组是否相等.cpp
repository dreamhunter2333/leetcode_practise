#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1662 lang=cpp
 *
 * [1662] 检查两个字符串数组是否相等
 */

// @lc code=start
class Solution
{
public:
    bool arrayStringsAreEqual(vector<string> &word1, vector<string> &word2)
    {
        auto join = [](vector<string> &word) -> string
        {
            string res = "";
            for (auto &&w : word)
            {
                res += w;
            }
            return res;
        };
        return join(word1) == join(word2);
    }
};
// @lc code=end
