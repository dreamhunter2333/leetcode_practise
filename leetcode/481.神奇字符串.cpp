#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=481 lang=cpp
 *
 * [481] 神奇字符串
 */

// @lc code=start
class Solution
{
public:
    int magicalString(int n)
    {
        if (n <= 3)
            return 1;
        vector<int> s;
        s.push_back(1);
        s.push_back(2);
        s.push_back(2);
        int res = 1;
        int num = 1;
        int i = 2;
        int j = 2;
        while (j < n)
        {
            // cout << i << "," << j << endl;
            for (size_t p = 0; p < s[i]; p++)
            {
                s.push_back(num);
                j++;
                if (num == 1 && j < n)
                    res++;
            }
            num = num == 2 ? 1 : 2;
            i++;
        }
        return res;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    int res = s.magicalString(6);
    cout << "res: " << res << endl;
    return 0;
}
