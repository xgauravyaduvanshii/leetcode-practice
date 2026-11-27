// LeetCode 2414. Length of the Longest Alphabetical Continuous Substring — Medium
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
// Submission 2204794580 — Accepted, C++
//
// My thinking: same idea as the Python version — one pass tracking the
// current run of consecutive letters; a break resets the run to 1, and
// the longest run seen is the answer.
class Solution {
public:
    int longestContinuousSubstring(string s) {
        int ans = 1;
        int cur = 1;
        for (int i = 1; i < (int)s.size(); i++) {
            if (s[i] == s[i - 1] + 1) {
                cur++;
            } else {
                cur = 1;
            }
            ans = max(ans, cur);
        }
        return ans;
    }
};
