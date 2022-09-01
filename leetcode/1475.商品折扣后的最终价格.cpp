#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1475 lang=cpp
 *
 * [1475] 商品折扣后的最终价格
 */

// @lc code=start
class Solution
{
public:
    vector<int> finalPrices(vector<int> &prices)
    {
        vector<int> res;
        int n = prices.size();
        for (size_t i = 0; i < n; i++)
        {
            int price = prices[i];
            for (size_t j = i + 1; j < n; j++)
            {
                if (prices[i] >= prices[j])
                {
                    price = prices[i] - prices[j];
                    break;
                }
            }
            res.push_back(price);
        }
        return res;
    }
};
// @lc code=end
