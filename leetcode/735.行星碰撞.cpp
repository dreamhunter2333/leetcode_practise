#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=735 lang=cpp
 *
 * [735] 行星碰撞
 */

// @lc code=start
class Solution
{
public:
    vector<int> asteroidCollision(vector<int> &asteroids)
    {
        vector<int> res;
        int i = 0;
        int n = asteroids.size();
        while (i < n)
        {
            int asteroid = asteroids[i];
            if (res.empty() || !(res.back() > 0 && asteroid < 0))
            {
                res.push_back(asteroid);
                i++;
                continue;
            }
            if ((-asteroid) > res.back())
            {
                res.pop_back();
                continue;
            }
            if ((-asteroid) == res.back())
            {
                res.pop_back();
            }
            i++;
        }
        return res;
    }
};
// @lc code=end
int main()
{
    Solution s;
    int arr[] = {5, 10, -5};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> asteroids(arr, arr + n);
    vector<int> res = s.asteroidCollision(asteroids);
    for (auto &&i : res)
    {
        cout << i << ",";
    }
    cout << endl;
}
