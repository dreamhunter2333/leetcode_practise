/*
 * @lc app=leetcode.cn id=1089 lang=cpp
 *
 * [1089] 复写零
 */
#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution
{
public:
    void duplicateZeros(vector<int> &arr)
    {
        int n = arr.size();
        int top = 0;
        int i = -1;
        int j = n - 1;
        while (top < n)
        {
            i++;
            top++;
            if (arr[i] == 0)
                top++;
        }
        if (top == n + 1)
        {
            arr[j] = 0;
            j--;
            i--;
        }
        while (j >= 0)
        {
            arr[j] = arr[i];
            if (arr[i] == 0)
            {
                arr[j - 1] = 0;
                j--;
            }
            j--;
            i--;
        }
    }
};
// @lc code=end
int main()
{
    Solution solution = Solution();
    int arr[] = {1, (int)0, 2, 3, 0, 4, 5, (int)0};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> vect(arr, arr + n);
    solution.duplicateZeros(vect);
    for (int i = 0; i < vect.size(); i++)
    {
        printf("%d,", vect[i]);
    }
}
