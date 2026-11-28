// LeetCode 2761. Prime Pairs With Target Sum — Medium
// https://leetcode.com/problems/prime-pairs-with-target-sum/
// Submission 2205243646 — Accepted, C++
//
// My thinking: same idea as the Python version — sieve up to
// n, then take every prime p up to n/2 whose complement n-p
// is also prime.
class Solution {
public:
    vector<vector<int>> findPrimePairs(int n) {
        vector<bool> isPrime(n + 1, true);
        if (n >= 0) isPrime[0] = false;
        if (n >= 1) isPrime[1] = false;
        for (int i = 2; i * 1LL * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) isPrime[j] = false;
            }
        }
        vector<vector<int>> ans;
        for (int p = 2; p <= n / 2; p++) {
            if (isPrime[p] && isPrime[n - p]) ans.push_back({p, n - p});
        }
        return ans;
    }
};
