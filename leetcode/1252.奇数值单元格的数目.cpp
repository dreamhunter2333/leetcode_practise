#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1252 lang=cpp
 *
 * [1252] 奇数值单元格的数目
 */

// @lc code=start
class Solution
{
public:
    int oddCells(int m, int n, vector<vector<int>> &indices)
    {
        int res = 0;
        int cache_m[m];
        memset(cache_m, 0, sizeof(cache_m));
        int cache_n[n];
        memset(cache_n, 0, sizeof(cache_n));
        for (auto &&i : indices)
        {
            cache_m[i[0]]++;
            cache_n[i[1]]++;
        }
        for (size_t r = 0; r < m; r++)
        {
            for (size_t c = 0; c < n; c++)
            {
                res += (cache_m[r] + cache_n[c]) % 2;
            }
        }
        return res;
    }
};
// @lc code=end
int main()
{
    Solution s;
    vector<vector<int>> vect;
    vector<int> vect1;
    vect1.push_back(0);
    vect1.push_back(1);
    vect.push_back(vect1);
    vector<int> vect2;
    vect2.push_back(1);
    vect2.push_back(1);
    vect.push_back(vect2);
    cout << s.oddCells(2, 3, vect) << endl;
}
