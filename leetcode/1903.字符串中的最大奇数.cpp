#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;
/*
 * @lc app=leetcode.cn id=1903 lang=cpp
 *
 * [1903] 字符串中的最大奇数
 */

// @lc code=start
class Solution
{
public:
    unordered_set<char> ODD{'1', '3', '5', '7', '9'};
    string largestOddNumber(string num)
    {
        for (int i = num.size() - 1; i >= 0; i--)
        {
            if (ODD.count(num[i]))
                return num.substr(0, i + 1);
        }
        return "";
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.largestOddNumber("52") << endl;
    cout << s.largestOddNumber("4206") << endl;
    cout << s.largestOddNumber("35427") << endl;
    return 0;
}
