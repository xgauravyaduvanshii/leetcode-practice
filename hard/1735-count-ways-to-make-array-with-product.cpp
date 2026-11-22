// LeetCode 1735. Count Ways to Make Array With Product — Hard
// https://leetcode.com/problems/count-ways-to-make-array-with-product/
// Submission 2201125958 — Accepted, C++
//
// My thinking: each prime power in k has to be split
// across the n slots, and splitting e identical copies
// into n slots is a stars-and-bars count — I multiply
// those counts, one prime at a time, modulo 1e9+7.

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;
    vector<int> waysToFillArray(vector<vector<int>>& queries) {
        int maxN = 0, maxK = 0;
        for (auto& q : queries) {
            maxN = max(maxN, q[0]);
            maxK = max(maxK, q[1]);
        }
        int N = maxN + 20;
        vector<long long> fact(N + 1, 1), invFact(N + 1, 1);
        for (int i = 1; i <= N; i++) fact[i] = fact[i - 1] * i % MOD;
        invFact[N] = modPow(fact[N], MOD - 2);
        for (int i = N; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
        auto comb = [&](int a, int b) -> long long {
            if (b < 0 || b > a) return 0;
            return fact[a] * invFact[b] % MOD * invFact[a - b] % MOD;
        };
        vector<int> spf(maxK + 1);
        for (int i = 0; i <= maxK; i++) spf[i] = i;
        for (int i = 2; i * i <= maxK; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxK; j += i) {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
        vector<int> answer;
        for (auto& q : queries) {
            int n = q[0], k = q[1];
            long long ways = 1;
            while (k > 1) {
                int p = spf[k], e = 0;
                while (k % p == 0) { k /= p; e++; }
                ways = ways * comb(n + e - 1, e) % MOD;
            }
            answer.push_back((int)ways);
        }
        return answer;
    }
private:
    long long modPow(long long base, long long exp) {
        long long res = 1;
        while (exp > 0) {
            if (exp & 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }
};
