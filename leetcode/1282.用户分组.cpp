#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=1282 lang=cpp
 *
 * [1282] 用户分组
 */

// @lc code=start
class Solution
{
public:
    vector<vector<int>> groupThePeople(vector<int> &groupSizes)
    {
        unordered_map<int, vector<int>> cache;
        for (size_t i = 0; i < groupSizes.size(); i++)
        {
            cache[groupSizes[i]].emplace_back(i);
        }
        vector<vector<int>> res;
        for (auto &&c : cache)
        {
            int count = c.second.size() / c.first;
            for (size_t i = 0; i < count; i++)
            {
                vector<int> group;
                for (size_t j = 0; j < c.first; j++)
                {
                    group.emplace_back(c.second[i * c.first + j]);
                }
                res.emplace_back(group);
            }
        }
        return res;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    int arr[] = {3, 3, 3, 3, 3, 1, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> vect(arr, arr + n);
    vector<vector<int>> res = s.groupThePeople(vect);
    cout << "[";
    for (auto &&v : res)
    {
        cout << "[";
        for (auto &&i : v)
        {
            cout << i << ",";
        }
        cout << "]";
    }
    cout << "]";
    cout << endl;
    return 0;
}
