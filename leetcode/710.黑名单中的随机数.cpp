#include <map>
#include <set>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=710 lang=cpp
 *
 * [710] 黑名单中的随机数
 */

// @lc code=start
class Solution
{
private:
    map<int, int> data;
    int bound;

public:
    Solution(int n, vector<int> &blacklist)
    {
        int m = blacklist.size();
        bound = n - m;
        int start = bound;
        set<int> blackSet;
        for (int b : blacklist)
        {
            if (b >= bound)
            {
                blackSet.emplace(b);
            }
        }
        for (auto &&b : blacklist)
        {
            if (b < bound)
            {
                while (blackSet.count(start))
                    start++;
                data[b] = start;
                start++;
            }
        }
    }

    int pick()
    {
        int res = rand() % bound;
        return data.count(res) ? data[res] : res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(n, blacklist);
 * int param_1 = obj->pick();
 */
// @lc code=end
