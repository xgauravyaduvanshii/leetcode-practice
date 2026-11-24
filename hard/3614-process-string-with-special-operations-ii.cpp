// LeetCode 3614. Process String with Special Operations II — Hard
// https://leetcode.com/problems/process-string-with-special-operations-ii/
// Submission 2202873633 — Accepted, C++
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string processStr(string s, long long k) {
        // My thinking: the result can grow to 10^15 characters, so
        // I never build it. I first record how long the result is
        // after each operation, capped above 10^15. Then I walk
        // backwards from the end: a letter answers the query when k
        // points at the position it appended, a '*' changes nothing,
        // a '#' maps k back into the first copy, and a '%' mirrors k
        // across the reversed string. If k is past the final length,
        // the answer is '.'.
        const long long INF = (long long)4e18;
        int n = s.size();
        vector<long long> lens(n);
        long long cur = 0;
        for (int i = 0; i < n; i++) {
            char ch = s[i];
            if (ch == '*') {
                cur = max(0LL, cur - 1);
            } else if (ch == '#') {
                cur = min(INF, cur * 2);
            } else if (ch == '%') {
                // unchanged
            } else {
                cur = min(INF, cur + 1);
            }
            lens[i] = cur;
        }
        if (k >= lens[n - 1]) return ".";
        for (int i = n - 1; i >= 0; i--) {
            char ch = s[i];
            long long prev = i > 0 ? lens[i - 1] : 0;
            if (ch == '*') {
                // nothing
            } else if (ch == '#') {
                if (prev > 0) k %= prev;
            } else if (ch == '%') {
                k = prev - 1 - k;
            } else {
                if (k == lens[i] - 1) return string(1, ch);
            }
        }
        return ".";
    }
};
