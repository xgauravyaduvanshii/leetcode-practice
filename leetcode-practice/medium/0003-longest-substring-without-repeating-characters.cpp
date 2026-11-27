// LeetCode 3. Longest Substring Without Repeating Characters — Medium
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Submission 2203751650 — Accepted, C++
//
// My thinking: I slide a window over the string, remembering the
// last index where each character was seen. When a repeat shows up
// inside the current window, I move the left edge to just past that
// character's previous spot, so the window never holds a duplicate.
// The best window length seen is the answer.

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int last[256];
        for (int i = 0; i < 256; i++) last[i] = -1;
        int left = 0, best = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            unsigned char ch = s[right];
            if (last[ch] >= left) left = last[ch] + 1;
            last[ch] = right;
            if (right - left + 1 > best) best = right - left + 1;
        }
        return best;
    }
};
