#include <iostream>
using namespace std;

/*
 * @lc app=leetcode.cn id=1108 lang=cpp
 *
 * [1108] IP 地址无效化
 */

// @lc code=start
class Solution
{
public:
    string defangIPaddr(string address)
    {
        string toReplace = "[.]";
        string search = ".";
        size_t pos = 0;
        while ((pos = address.find(search, pos)) != string::npos)
        {
            address.replace(pos, search.length(), toReplace);
            pos += toReplace.length();
        }
        return address;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution solution = Solution();
    cout << solution.defangIPaddr("1.1.1.1") << endl;
    return 0;
}
