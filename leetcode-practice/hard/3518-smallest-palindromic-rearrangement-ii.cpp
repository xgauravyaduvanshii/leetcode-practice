// LeetCode 3518. Smallest Palindromic Rearrangement II — Hard
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
// Submission 2202796428 — Accepted, C++
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string smallestPalindrome(string s, int k) {
        // My thinking: a palindromic permutation is fixed by its first
        // half, which is a permutation of the halved character counts
        // (the odd-count letter, if any, sits in the middle). I first
        // check whether there are at least k distinct first halves at
        // all — if not, the answer is empty. Otherwise I build the
        // first half greedily, trying letters from 'a' upward and
        // taking a letter only when the permutations of what is left
        // are at least k; if fewer, I skip that many and move on.
        // All combination counts are exact integers capped at k + 1,
        // so no floating-point rounding can creep in.
        vector<long long> half(26, 0);
        char mid = 0;
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        for (int i = 0; i < 26; i++) {
            half[i] = cnt[i] / 2;
            if (cnt[i] % 2 == 1) mid = (char)('a' + i);
        }
        long long m = 0;
        for (long long v : half) m += v;
        long long LIMIT = (long long)k + 1;
        auto binom_cap = [&](long long n, long long r) {
            if (r > n - r) r = n - r;
            __int128 res = 1;
            for (long long i = 1; i <= r; i++) {
                res = res * (n - r + i) / i;
                if (res > LIMIT) return LIMIT + 1;
            }
            return (long long)res;
        };
        auto count_perms = [&](const vector<long long>& counts) {
            long long res = 1;
            long long remaining = 0;
            for (long long v : counts) remaining += v;
            for (int i = 0; i < 26; i++) {
                long long c = counts[i];
                if (c == 0) continue;
                long long b = binom_cap(remaining, c);
                if (b > LIMIT) return LIMIT;
                __int128 prod = (__int128)res * b;
                if (prod >= LIMIT) return LIMIT;
                res = (long long)prod;
                remaining -= c;
            }
            return res;
        };
        if (count_perms(half) < k) return "";
        string first;
        vector<long long> rem = half;
        for (long long pos = 0; pos < m; pos++) {
            for (int i = 0; i < 26; i++) {
                if (rem[i] == 0) continue;
                rem[i]--;
                long long c = count_perms(rem);
                if (c >= k) {
                    first.push_back((char)('a' + i));
                    break;
                }
                k -= (int)c;
                rem[i]++;
            }
        }
        string ans = first;
        if (mid) ans.push_back(mid);
        reverse(first.begin(), first.end());
        ans += first;
        return ans;
    }
};
