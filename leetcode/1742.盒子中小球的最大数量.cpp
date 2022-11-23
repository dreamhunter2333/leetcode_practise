#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;
/*
 * @lc app=leetcode.cn id=1742 lang=cpp
 *
 * [1742] 盒子中小球的最大数量
 */

// @lc code=start
class Solution
{
public:
    int countBalls(int lowLimit, int highLimit)
    {
        unordered_map<int, int> count_map;
        int a = 0;
        for (int i = lowLimit; i <= highLimit; i++)
        {
            int target = 0;
            int num = i;
            while (num > 0)
            {
                target += (num % 10);
                num = (num / 10);
            }
            count_map[target] += 1;
        }
        auto res = max_element(count_map.begin(), count_map.end(), [](const pair<int, int> &a, const pair<int, int> &b) -> bool
                               { return a.second < b.second; });
        return res->second;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.countBalls(1, 10) << "\n";
    cout << s.countBalls(5, 15) << "\n";
    cout << s.countBalls(19, 28) << endl;
    return 0;
}
