#include <istream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1450 lang=cpp
 *
 * [1450] 在既定时间做作业的学生人数
 */

// @lc code=start
class Solution
{
public:
    int busyStudent(vector<int> &startTime, vector<int> &endTime, int queryTime)
    {
        int res = 0;
        for (size_t i = 0; i < startTime.size(); i++)
        {
            if (startTime[i] <= queryTime && queryTime <= endTime[i])
                res++;
        }
        return res;
    }
};
// @lc code=end
