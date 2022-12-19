#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1971 lang=cpp
 *
 * [1971] 寻找图中是否存在路径
 */

// @lc code=start
class Solution
{
public:
    bool validPath(int n, vector<vector<int>> &edges, int source, int destination)
    {
        if (source == destination)
            return true;
        vector<int> p(n);
        for (size_t i = 0; i < n; i++)
            p[i] = i;

        function<int(int)> find;
        find = [&](int x) -> int
        {
            if (x != p[x])
                p[x] = find(p[x]);
            return p[x];
        };
        for (auto &&edge : edges)
        {
            int root_x = find(edge[0]);
            int root_y = find(edge[1]);
            if (root_x == root_y)
                continue;
            p[root_y] = root_x;
        }
        return find(source) == find(destination);
    }
};

// @lc code=end
int main(int argc, char const *argv[])
{
    Solution s;
    vector<vector<int>> edges({{0, 1}, {1, 2}, {2, 0}});
    cout << s.validPath(3, edges, 0, 2) << endl;
    return 0;
}
