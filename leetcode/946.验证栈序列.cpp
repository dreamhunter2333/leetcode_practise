#include <iostream>
#include <vector>
#include <set>
using namespace std;
/*
 * @lc app=leetcode.cn id=946 lang=cpp
 *
 * [946] 验证栈序列
 */

// @lc code=start
class Solution
{
public:
    bool validateStackSequences(vector<int> &pushed, vector<int> &popped)
    {
        vector<int> stack;
        set<int> cache_set;
        int i = 0;
        int n = popped.size();
        for (auto &&num : pushed)
        {
            stack.push_back(num);
            cache_set.emplace(num);
            while (i < n && cache_set.count(popped[i]))
            {
                if (popped[i] != stack.back())
                    return false;
                stack.pop_back();
                i++;
            }
        }
        return true;
    }
};
// @lc code=end
