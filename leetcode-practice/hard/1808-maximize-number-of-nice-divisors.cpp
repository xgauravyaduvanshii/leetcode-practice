// LeetCode 1808. Maximize Number of Nice Divisors — Hard
// https://leetcode.com/problems/maximize-number-of-nice-divisors/
// Submission 2201178975 — Accepted, C++
//
// My thinking: the nice divisors multiply out as
// the product of the exponents, so I split the
// prime factors into threes — a leftover one is
// better spent as two twos than as a three and a
// one.

#include <vector>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;

    long long modPow(long long base, long long exp) {
        long long res = 1;
        while (exp > 0) {
            if (exp & 1) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1;
        }
        return res;
    }

    int maxNiceDivisors(int primeFactors) {
        if (primeFactors == 1) return 1;
        long long q = primeFactors / 3;
        int r = primeFactors % 3;
        if (r == 0) return (int)modPow(3, q);
        if (r == 1) return (int)(modPow(3, q - 1) * 4 % MOD);
        return (int)(modPow(3, q) * 2 % MOD);
    }
};
