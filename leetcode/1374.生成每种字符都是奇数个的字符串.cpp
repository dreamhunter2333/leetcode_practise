#include <iostream>
using namespace std;
/*
 * @lc app=leetcode.cn id=1374 lang=cpp
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
class Solution
{
public:
    string generateTheString(int n)
    {
        string res(n - 1, 'a');
        return res + (n % 2 ? "a" : "b");
    }
};
// @lc code=end
