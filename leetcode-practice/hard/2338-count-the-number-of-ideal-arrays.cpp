// LeetCode 2338. Count the Number of Ideal Arrays — Hard
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/
// Submission 2201688891 — Accepted, C++
//
// My thinking: an ideal array is a chain
// of divisors stretched over the slots — I
// count how many chains of each length
// exist, then choose where each new value
// first appears.

#include <numeric>
#include <vector>
using namespace std;

const int MOD = 1000000007;

long long modPow(long long a, long long e) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % MOD;
        a = a * a % MOD;
        e >>= 1;
    }
    return r;
}

class Solution {
public:
    int idealArrays(int n, int maxValue) {
        vector<long long> fact(n + 1, 1), invFact(n + 1, 1);
        for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[n] = modPow(fact[n], MOD - 2);
        for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        auto comb = [&](int a, int b) -> long long {
            if (b < 0 || b > a) return 0;
            return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
        };
        vector<long long> dp(maxValue + 1, 1), chains;
        chains.push_back(0);
        chains.push_back(maxValue);
        while (true) {
            vector<long long> ndp(maxValue + 1, 0);
            for (int u = 1; u <= maxValue; u++) {
                if (dp[u] == 0) continue;
                for (int m = u * 2; m <= maxValue; m += u) {
                    ndp[m] = (ndp[m] + dp[u]) % MOD;
                }
            }
            long long total = 0;
            for (int v = 1; v <= maxValue; v++) total = (total + ndp[v]) % MOD;
            if (total == 0) break;
            chains.push_back(total);
            dp = ndp;
        }
        long long ans = 0;
        for (int k = 1; k < (int)chains.size(); k++) {
            ans = (ans + chains[k] * comb(n - 1, k - 1)) % MOD;
        }
        return (int)ans;
    }
};
