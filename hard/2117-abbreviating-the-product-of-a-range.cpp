// LeetCode 2117. Abbreviating the Product of a Range — Hard
// https://leetcode.com/problems/abbreviating-the-product-of-a-range/
// Submission 2201579202 — Accepted, C++
//
// My thinking: the middle of the product is
// far too big to write out, so I keep only
// what the answer needs — the trailing zeros
// counted off as an exponent, the last five
// digits kept exactly, and the first five read
// off the size of the number instead of the
// number itself.

#include <cmath>
#include <string>
using namespace std;

class Solution {
public:
    string abbreviateProduct(int left, int right) {
        long long total2 = 0, total5 = 0;
        double logSum = 0.0;
        long long stripped = 1;
        for (int x = left; x <= right; ++x) {
            logSum += log10((double)x);
            int v = x;
            while (v % 2 == 0) {
                v /= 2;
                ++total2;
            }
            while (v % 5 == 0) {
                v /= 5;
                ++total5;
            }
            stripped = (stripped * v) % 100000;
        }
        long long zeros = min(total2, total5);
        long long suffix = stripped;
        if (total2 > zeros) {
            suffix = (suffix * modPow(2, total2 - zeros)) % 100000;
        } else if (total5 > zeros) {
            suffix = (suffix * modPow(5, total5 - zeros)) % 100000;
        }
        double logY = logSum - (double)zeros;
        long long digits = (long long)logY + 1;
        if (digits <= 10) {
            // Small enough to write out exactly.
            long long exact = 1;
            for (int x = left; x <= right; ++x) {
                int v = x;
                while (v % 2 == 0) v /= 2;
                while (v % 5 == 0) v /= 5;
                exact *= v;
            }
            if (total2 > zeros) {
                long long p = 1;
                for (long long i = 0; i < total2 - zeros; ++i) p *= 2;
                exact *= p;
            } else if (total5 > zeros) {
                long long p = 1;
                for (long long i = 0; i < total5 - zeros; ++i) p *= 5;
                exact *= p;
            }
            return to_string(exact) + "e" + to_string(zeros);
        }
        double frac = logY - (long long)logY;
        long long prefix = (long long)pow(10.0, frac + 4);
        string suf = to_string(suffix);
        suf = string(5 - suf.size(), '0') + suf;
        return to_string(prefix) + "..." + suf + "e" + to_string(zeros);
    }

private:
    long long modPow(long long base, long long exp) {
        long long res = 1;
        while (exp > 0) {
            if (exp & 1) res = (res * base) % 100000;
            base = (base * base) % 100000;
            exp >>= 1;
        }
        return res;
    }
};
