#include <iostream>
#include <vector>
using namespace std;
/*
 * @lc app=leetcode.cn id=1455 lang=cpp
 *
 * [1455] 检查单词是否为句中其他单词的前缀
 */

// @lc code=start
class Solution
{
public:
    int isPrefixOfWord(string sentence, string searchWord)
    {
        string temp = "";
        int i = 1;
        for (auto &&letter : sentence)
        {
            if (letter == ' ')
            {
                if (temp.rfind(searchWord, 0) == 0)
                    return i;
                temp = "";
                i += 1;
            }
            else
            {
                temp += letter;
            }
        }
        if (temp.rfind(searchWord, 0) == 0)
            return i;
        return -1;
    }
};
// @lc code=end
