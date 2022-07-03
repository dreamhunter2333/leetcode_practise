#include <iostream>
#include <unordered_map>
using namespace std;
/*
 * @lc app=leetcode.cn id=535 lang=cpp
 *
 * [535] TinyURL 的加密与解密
 */

// @lc code=start
class Solution
{
private:
    unordered_map<int, string> data;
    int max_id = 0;

public:
    // Encodes a URL to a shortened URL.
    string encode(string longUrl)
    {
        max_id++;
        data[max_id] = longUrl;
        return "http://tinyurl.com/" + to_string(max_id);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl)
    {
        string data_id = shortUrl;
        size_t pos;
        string delimiter = "/";
        while ((pos = data_id.find(delimiter)) != string::npos)
        {
            data_id.erase(0, pos + delimiter.length());
        }
        return data[std::stoi(data_id)];
    }
};

// @lc code=end
int main()
{
    string url = "https://leetcode.com/problems/design-tinyurl";
    Solution solution;
    return url != solution.decode(solution.encode(url));
}
