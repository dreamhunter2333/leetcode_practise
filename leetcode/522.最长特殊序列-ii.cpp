#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=522 lang=cpp
 *
 * [522] 最长特殊序列 II
 */

// @lc code=start
class Solution
{
public:
    int findLUSlength(vector<string> &strs)
    {
        int res = -1;
        int n = strs.size();
        for (size_t i = 0; i < n; i++)
        {
            bool check = true;
            for (size_t j = 0; j < n; j++)
            {
                if (i != j && is_sub(strs[j], strs[i]))
                {
                    check = false;
                    break;
                }
            }
            if (check)
                res = max(res, static_cast<int>(strs[i].size()));
        }
        return res;
    }
    bool is_sub(string &word1, string &word2)
    {
        int i = 0, j = 0;
        int n = word1.size();
        int m = word2.size();
        while (i < n && j < m)
        {
            if (word1[i] == word2[j])
                j++;
            i++;
        }
        return j == m;
    }
};
// @lc code=end
int main()
{
    Solution s = Solution();
    string strs[] = {"aba", "cdc", "eae"};
    vector<string> vect(strs, strs + 3);
    cout << s.findLUSlength(vect) << endl;
}
