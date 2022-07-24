#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
/*
 * @lc app=leetcode.cn id=1184 lang=cpp
 *
 * [1184] 公交站间的距离
 */

// @lc code=start
class Solution
{
public:
    int distanceBetweenBusStops(vector<int> &distance, int start, int destination)
    {
        int res = 0;
        int all_distance = accumulate(distance.begin(), distance.end(), 0);
        if (start > destination)
            swap(start, destination);
        for (int i = start; i < destination; i++)
            res += distance[i];
        return min(res, all_distance - res);
    }
};
// @lc code=end
int main()
{
    Solution s;
    int arr[] = {1, 2, 3, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> vect(arr, arr + n);
    cout << s.distanceBetweenBusStops(vect, 0, 1) << endl;
    int arr2[] = {1, 2, 3, 4};
    int n2 = sizeof(arr) / sizeof(arr[0]);
    vector<int> vect2(arr2, arr2 + n2);
    cout << s.distanceBetweenBusStops(vect2, 0, 2) << endl;
}
