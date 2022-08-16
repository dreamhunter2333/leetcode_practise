#include <iostream>
#include <string>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1656 lang=cpp
 *
 * [1656] 设计有序流
 */

// @lc code=start
class OrderedStream
{
private:
    string *arr;
    int size = 0;
    int ptr = 0;

public:
    OrderedStream(int n)
    {
        arr = new string[n];
        size = n;
        ptr = 0;
    }

    vector<string> insert(int idKey, string value)
    {
        arr[idKey - 1] = value;
        vector<string> res;
        for (size_t i = ptr; i < size; i++)
        {
            if (arr[i] == "")
                break;
            res.push_back(arr[i]);
            ptr++;
        }
        return res;
    }
};

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream* obj = new OrderedStream(n);
 * vector<string> param_1 = obj->insert(idKey,value);
 */
// @lc code=end
