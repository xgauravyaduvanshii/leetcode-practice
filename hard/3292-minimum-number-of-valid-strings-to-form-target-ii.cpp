// LeetCode 3292. Minimum Number of Valid Strings to Form Target II — Hard
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/
// Submission 2202185276 — Accepted, C++
//
// My thinking: a valid string is any prefix of
// any word, so I hash every word prefix once.
// For each target position I binary-search the
// longest prefix that matches there (rolling
// hashes make each check O(1)), then greedily
// jump: always extend the current string as far
// as it can reach, which is optimal for the
// minimum number of strings.

class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        const long long MOD1 = 1000000007LL;
        const long long MOD2 = 1000000009LL;
        const long long BASE = 131;
        unordered_set<long long> pref;
        pref.reserve(100000);
        int maxLen = 0;
        for (auto &w : words) {
            maxLen = max(maxLen, (int)w.size());
            long long h1 = 0, h2 = 0;
            for (char ch : w) {
                long long v = ch - 'a' + 1;
                h1 = (h1 * BASE + v) % MOD1;
                h2 = (h2 * BASE + v) % MOD2;
                pref.insert((h1 << 32) | h2);
            }
        }
        int n = (int)target.size();
        vector<long long> pow1(n + 1), pow2(n + 1), ph1(n + 1), ph2(n + 1);
        pow1[0] = pow2[0] = 1;
        for (int i = 0; i < n; i++) {
            pow1[i + 1] = pow1[i] * BASE % MOD1;
            pow2[i + 1] = pow2[i] * BASE % MOD2;
            long long v = target[i] - 'a' + 1;
            ph1[i + 1] = (ph1[i] * BASE + v) % MOD1;
            ph2[i + 1] = (ph2[i] * BASE + v) % MOD2;
        }
        auto subHash = [&](int i, int len) -> long long {
            long long h1 = (ph1[i + len] - ph1[i] * pow1[len]) % MOD1;
            if (h1 < 0) h1 += MOD1;
            long long h2 = (ph2[i + len] - ph2[i] * pow2[len]) % MOD2;
            if (h2 < 0) h2 += MOD2;
            return (h1 << 32) | h2;
        };
        auto longest = [&](int i) -> int {
            int lo = 0, hi = min(maxLen, n - i);
            while (lo < hi) {
                int mid = (lo + hi + 1) / 2;
                if (pref.find(subHash(i, mid)) != pref.end()) lo = mid;
                else hi = mid - 1;
            }
            return lo;
        };
        int jumps = 0, curEnd = 0, farthest = 0;
        for (int i = 0; i < n; i++) {
            if (i > farthest) return -1;
            farthest = max(farthest, i + longest(i));
            if (i == curEnd) {
                if (farthest <= i) return -1;
                jumps++;
                curEnd = farthest;
                if (curEnd >= n) return jumps;
            }
        }
        return -1;
    }
};
