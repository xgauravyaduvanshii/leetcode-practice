// LeetCode 3704. Count No-Zero Pairs That Sum to N — Hard
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/
// Submission 2203055723 — Accepted, C++
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    long long countNoZeroPairs(long long n) {
        // My thinking: a no-zero number has no zero digit at any
        // position below its most significant digit, so while I
        // scan the digits of n from least to most significant I
        // only need to know, for each of a and b, whether it is
        // still "active" (all its digits so far are 1..9 and it
        // may continue) or has "ended" (its higher digits are all
        // blank). The units digit of each must be 1..9 — a zero
        // there would mean the number is 0 or has an interior
        // zero. At each position I try every digit pair that fits
        // the digit of n plus the carry, and carry the rest.
        string s = to_string(n);
        int L = (int)s.size();
        vector<int> digits(L);
        for (int i = 0; i < L; i++) digits[i] = s[L - 1 - i] - '0';
        // dp[carry][a_active][b_active]
        long long dp[2][2][2] = {};
        dp[0][1][1] = 1;
        for (int i = 0; i < L; i++) {
            long long ndp[2][2][2] = {};
            for (int carry = 0; carry < 2; carry++) {
                for (int aActive = 0; aActive < 2; aActive++) {
                    for (int bActive = 0; bActive < 2; bActive++) {
                        long long cur = dp[carry][aActive][bActive];
                        if (cur == 0) continue;
                        for (int da = 0; da <= 9; da++) {
                            if (!digitAllowed(da, aActive, i)) continue;
                            for (int db = 0; db <= 9; db++) {
                                if (!digitAllowed(db, bActive, i)) continue;
                                int sum = da + db + carry;
                                if (sum % 10 != digits[i]) continue;
                                int na = da > 0 ? 1 : 0;
                                int nb = db > 0 ? 1 : 0;
                                ndp[sum / 10][na][nb] += cur;
                            }
                        }
                    }
                }
            }
            for (int c = 0; c < 2; c++)
                for (int a = 0; a < 2; a++)
                    for (int b = 0; b < 2; b++)
                        dp[c][a][b] = ndp[c][a][b];
        }
        // After the most significant digit the carry must be 0;
        // a and b may be active or ended, both are valid.
        long long ans = 0;
        for (int a = 0; a < 2; a++)
            for (int b = 0; b < 2; b++)
                ans += dp[0][a][b];
        return ans;
    }

private:
    // Digits allowed at this position: an ended number only
    // contributes a blank 0; an active number takes 1..9 at
    // the units place (it must have a units digit) and 0..9
    // above it, where 0 means it ends here.
    bool digitAllowed(int d, int active, int pos) {
        if (active == 0) return d == 0;
        if (pos == 0) return d >= 1;
        return true;
    }
};
