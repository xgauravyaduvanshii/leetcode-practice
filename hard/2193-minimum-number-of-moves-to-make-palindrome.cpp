// LeetCode 2193. Minimum Number of Moves to Make Palindrome — Hard
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
// Submission 2201614376 — Accepted, C++
//
// My thinking: work from the two ends in —
// matching ends just close in, a letter with
// a partner further in gets walked over to
// its end, and the one letter with no partner
// shuffles one step toward the middle at a
// time.

#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int minMovesToMakePalindrome(string s) {
        unordered_map<char, int> freq;
        for (char c : s) freq[c]++;
        int odd = 0;
        for (auto& [c, cnt] : freq) {
            if (cnt % 2 == 1) odd++;
        }
        if (odd > 1) return -1;
        int ans = 0;
        int left = 0, right = (int)s.size() - 1;
        while (left < right) {
            if (s[left] == s[right]) {
                left++;
                right--;
            } else {
                int k = right;
                while (k > left && s[k] != s[left]) k--;
                if (k == left) {
                    // s[left] is the odd one out; nudge it toward the middle.
                    swap(s[left], s[left + 1]);
                    ans++;
                } else {
                    while (k < right) {
                        swap(s[k], s[k + 1]);
                        k++;
                        ans++;
                    }
                    left++;
                    right--;
                }
            }
        }
        return ans;
    }
};
