#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=1636 lang=cpp
 *
 * [1636] 按照频率将数组升序排序
 */

// @lc code=start
class Solution
{
public:
    vector<int> frequencySort(vector<int> &nums)
    {
        unordered_map<int, int> nums_counter;
        for (auto &&num : nums)
            nums_counter[num]++;

        sort(nums.begin(), nums.end(), [nums_counter](const int &a, const int &b)
             {
                if (nums_counter.at(a) == nums_counter.at(b)) return a > b;
                return nums_counter.at(a) < nums_counter.at(b); });
        return nums;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution s = Solution();
    int nums[] = {1, 1, 2, 2, 2, 3};
    vector<int> vect(nums, nums + 6);
    vector<int> res = s.frequencySort(vect);
    cout << "[";
    for (auto &&v : res)
    {
        cout << v << ",";
    }
    cout << "]";
    cout << endl;
    return 0;
}
