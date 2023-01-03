#include <iostream>
#include <string>
#include <sstream> // std::stringstream
using namespace std;
/*
 * @lc app=leetcode.cn id=2042 lang=cpp
 *
 * [2042] 检查句子中的数字是否递增
 */

// @lc code=start
bool isdigit(string tmp)
{
    for (auto &&c : tmp)
    {
        if (!isdigit(c))
            return false;
    }
    return true;
}

class Solution
{
public:
    bool areNumbersAscending(string s)
    {
        int pre = -1;
        string tmp;
        stringstream ss(s);
        while (getline(ss, tmp, ' '))
        {
            if (!isdigit(tmp))
                continue;
            int num = stoi(tmp);
            if (num <= pre)
                return false;
            pre = num;
        }
        return true;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.areNumbersAscending("4 5 11 26") << endl;
    return 0;
}
