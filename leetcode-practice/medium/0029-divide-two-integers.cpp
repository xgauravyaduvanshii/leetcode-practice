// LeetCode 29. Divide Two Integers — Medium
// https://leetcode.com/problems/divide-two-integers/
// Submission 2203814665 — Accepted, C++

// My thinking: I work with the absolute values and double the divisor
// by shifting left, finding the biggest doubled chunk that still fits
// into what is left of the dividend. Each chunk I take adds its power
// of two to the answer, then I keep going with the remainder. The sign
// goes on at the end, and the one overflow case (-2^31 divided by -1)
// is clamped to 2^31 - 1.
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        bool negative = (dividend < 0) != (divisor < 0);
        long a = labs(dividend), b = labs(divisor);
        long quotient = 0;
        while (a >= b) {
            long chunk = b, multiple = 1;
            while (a >= (chunk << 1)) {
                chunk <<= 1;
                multiple <<= 1;
            }
            a -= chunk;
            quotient += multiple;
        }
        return negative ? -quotient : quotient;
    }
};
