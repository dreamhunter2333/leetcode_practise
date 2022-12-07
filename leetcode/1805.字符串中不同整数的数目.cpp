#include <iostream>
#include <set>
#include <deque>
using namespace std;
/*
 * @lc app=leetcode.cn id=1805 lang=cpp
 *
 * [1805] 字符串中不同整数的数目
 */

// @lc code=start
class Solution
{
public:
    int numDifferentIntegers(string word)
    {
        word += "a";
        set<string> res;
        deque<char> pre;
        for (auto &&lett : word)
        {
            if (isdigit(lett))
            {
                if (!pre.empty() && pre.front() == '0')
                    pre.pop_front();
                pre.push_back(lett);
            }
            else if (!pre.empty())
            {
                string pre_str(pre.begin(), pre.end());
                res.emplace(pre_str);
                pre.clear();
            }
            else
            {
                pre.clear();
            }
        }
        return res.size();
    }
};
// @lc code=end
