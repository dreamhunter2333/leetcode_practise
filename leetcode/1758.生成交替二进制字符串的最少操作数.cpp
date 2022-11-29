#include <iostream>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=1758 lang=cpp
 *
 * [1758] 生成交替二进制字符串的最少操作数
 */

// @lc code=start
class Solution
{
public:
    int minOperations(string s)
    {
        unordered_map<char, char> bit_map;
        bit_map['1'] = '0';
        bit_map['0'] = '1';
        char bit = '0';
        int count = 0;
        for (auto &&c : s)
        {
            if (bit == c)
                count++;
            bit = bit_map[bit];
        }
        return min(count, (int)s.size() - count);
    }
};
// @lc code=end
