// LeetCode 3448. Count Substrings Divisible By Last Digit — Hard
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/
// Submission 2202543646 — Accepted 699/699, C++
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    long long countSubstrings(string s) {
        // My thinking: for each divisor d, keep how many substrings
        // ending at the previous position have each value mod d.
        // Extending them by one digit maps every residue v to
        // (v * 10 + digit) % d, and the new single digit starts a
        // fresh substring; when the last digit is d itself, the
        // substrings with residue 0 are the ones that count.
        int n = (int)s.size();
        long long ans = 0;
        vector<vector<long long>> cnt(10);
        for (int d = 1; d <= 9; ++d) cnt[d].assign(d, 0);
        for (int j = 0; j < n; ++j) {
            int dig = s[j] - '0';
            for (int d = 1; d <= 9; ++d) {
                vector<long long> nxt(d, 0);
                for (int v = 0; v < d; ++v) {
                    nxt[(v * 10 + dig) % d] += cnt[d][v];
                }
                nxt[dig % d] += 1;
                cnt[d].swap(nxt);
                if (dig == d) ans += cnt[d][0];
            }
        }
        return ans;
    }
};
