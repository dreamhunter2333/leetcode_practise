#include <iostream>
using namespace std;
/*
 * @lc app=leetcode.cn id=2180 lang=cpp
 *
 * [2180] 统计各位数字之和为偶数的整数个数
 */

// @lc code=start
class Solution
{
public:
    int countEven(int num)
    {
        int res = 0;
        for (size_t i = 1; i <= num; i++)
        {
            int sum_i = 0;
            int tmp = i;
            while (tmp > 0)
            {
                sum_i += tmp % 10;
                tmp = tmp / 10;
            }
            if (sum_i % 2 == 0)
                res += 1;
        }
        return res;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.countEven(4) << endl;
    cout << s.countEven(30) << endl;
    return 0;
}
