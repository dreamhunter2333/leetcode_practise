#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;
/*
 * @lc app=leetcode.cn id=2309 lang=cpp
 *
 * [2309] 兼具大小写的最好英文字母
 */

// @lc code=start
class Solution
{
public:
    string greatestLetter(string s)
    {
        unordered_set<char> ht(s.begin(), s.end());
        for (int i = 25; i >= 0; i--)
        {
            if (ht.count('a' + i) > 0 && ht.count('A' + i) > 0)
            {
                return string(1, 'A' + i);
            }
        }
        return "";
    }
};
// @lc code=end
