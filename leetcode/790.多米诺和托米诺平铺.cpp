#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=790 lang=cpp
 *
 * [790] 多米诺和托米诺平铺
 */

// @lc code=start
class Solution
{
public:
    int numTilings(int n)
    {
        const long long mod = 1e9 + 7;
        vector<vector<long long>> dp(n, vector<long long>(4));
        dp[0][0] = dp[0][1] = 1;
        for (int i = 1; i < n; i++)
        {
            dp[i][0] = dp[i - 1][1];
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % mod;
            dp[i][2] = (dp[i - 1][0] + dp[i - 1][3]) % mod;
            dp[i][3] = (dp[i - 1][0] + dp[i - 1][2]) % mod;
        }
        return dp[n - 1][1];
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.numTilings(3) << endl;
    return 0;
}
