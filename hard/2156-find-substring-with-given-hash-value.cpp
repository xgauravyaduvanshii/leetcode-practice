// LeetCode 2156. Find Substring With Given Hash Value — Hard
// https://leetcode.com/problems/find-substring-with-given-hash-value/
// Submission 2201593564 — Accepted, C++
//
// My thinking: the hash reads the substring
// left to right with rising powers, so sliding
// it one step left means dropping the far
// letter, shifting everything up a power, and
// adding the new first letter — and sweeping
// from the right keeps the smallest index that
// matches.

#include <string>
using namespace std;

class Solution {
public:
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        int n = (int)s.size();
        auto val = [](char c) { return c - 'a' + 1; };
        long long pk = modPow(power, k, modulo);
        long long h = 0;
        for (int i = n - k; i < n; ++i) {
            h = (h + val(s[i]) * modPow(power, i - (n - k), modulo)) % modulo;
        }
        int ans = (h == hashValue) ? n - k : -1;
        for (int i = n - k - 1; i >= 0; --i) {
            h = (val(s[i]) + (long long)power * h - val(s[i + k]) * pk) % modulo;
            if (h < 0) h += modulo;
            if (h == hashValue) ans = i;
        }
        return s.substr(ans, k);
    }

private:
    long long modPow(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
};
