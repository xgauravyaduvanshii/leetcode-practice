// LeetCode 2514. Count Anagrams — Hard
// https://leetcode.com/problems/count-anagrams/
// Submission 2201793250 — Accepted, C++
//
// My thinking: each word stands on its
// own — its distinct shuffles are its
// length factorial divided by the
// factorial of every repeated letter —
// and the words multiply together.

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countAnagrams(string s) {
        const int MOD = 1000000007;
        vector<long long> fact(100001, 1);
        for (int i = 1; i <= 100000; i++) fact[i] = fact[i - 1] * i % MOD;
        auto modpow = [&](long long a, long long e) {
            long long r = 1;
            while (e) {
                if (e & 1) r = r * a % MOD;
                a = a * a % MOD;
                e >>= 1;
            }
            return r;
        };
        long long ans = 1;
        int n = (int)s.size(), i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] != ' ') j++;
            int len = j - i;
            vector<int> cnt(26, 0);
            for (int t = i; t < j; t++) cnt[s[t] - 'a']++;
            long long ways = fact[len];
            for (int c : cnt) ways = ways * modpow(fact[c], MOD - 2) % MOD;
            ans = ans * ways % MOD;
            i = j + 1;
        }
        return (int)ans;
    }
};
