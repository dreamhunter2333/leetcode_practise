#include <iostream>
#include <string>
using namespace std;
/*
 * @lc app=leetcode.cn id=1812 lang=cpp
 *
 * [1812] 判断国际象棋棋盘中一个格子的颜色
 */

// @lc code=start
class Solution
{
public:
    bool squareIsWhite(string coordinates)
    {
        return ((coordinates[0] - 'a' + 1 +
                 (int)coordinates[1] - '0') %
                2) == 1;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.squareIsWhite("a1") << endl;
    cout << s.squareIsWhite("h3") << endl;
    cout << s.squareIsWhite("c7") << endl;
    return 0;
}
