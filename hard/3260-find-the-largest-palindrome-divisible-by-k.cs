// LeetCode 3260. Find the Largest Palindrome Divisible by K — Hard
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/
// Submission 2202155914 — Accepted, C#
//
// My thinking: only the first half of the
// palindrome is free — each of its digits
// contributes a known coefficient mod k (its
// two mirrored powers of 10, or one for the
// middle digit). I precompute, for each
// position, the set of remainders the suffix
// can still reach as a bitmask, then greedily
// pick the largest digit at each position that
// leaves a completable remainder.

public class Solution {
    public string LargestPalindrome(int n, int k) {
        int h = (n + 1) / 2;
        int[] pow10 = new int[n];
        pow10[0] = 1 % k;
        for (int i = 1; i < n; i++) pow10[i] = (pow10[i - 1] * 10) % k;
        int[] coeff = new int[h];
        for (int i = 0; i < h; i++) {
            if (n % 2 == 1 && i == h - 1) coeff[i] = pow10[n - 1 - i];
            else coeff[i] = (pow10[n - 1 - i] + pow10[i]) % k;
        }
        int full = (1 << k) - 1;
        int[] suff = new int[h + 1];
        suff[h] = 1;
        for (int i = h - 1; i >= 0; i--) {
            int mask = 0;
            int nxt = suff[i + 1];
            int c = coeff[i];
            bool[] seen = new bool[10];
            for (int d = 0; d < 10; d++) {
                int shift = (d * c) % k;
                if (seen[shift]) continue;
                seen[shift] = true;
                int rot;
                if (shift == 0) rot = nxt;
                else rot = ((nxt << shift) & full) | (nxt >> (k - shift));
                mask |= rot;
            }
            suff[i] = mask;
        }
        char[] half = new char[h];
        int acc = 0;
        for (int i = 0; i < h; i++) {
            int lo = i == 0 ? 1 : 0;
            for (int d = 9; d >= lo; d--) {
                int need = ((-acc - d * coeff[i]) % k + k) % k;
                if (((suff[i + 1] >> need) & 1) == 1) {
                    half[i] = (char)('0' + d);
                    acc = (acc + d * coeff[i]) % k;
                    break;
                }
            }
        }
        string halfS = new string(half);
        if (n % 2 == 1) {
            char[] rev = halfS.Substring(0, h - 1).ToCharArray();
            Array.Reverse(rev);
            return halfS + new string(rev);
        } else {
            char[] rev = halfS.ToCharArray();
            Array.Reverse(rev);
            return halfS + new string(rev);
        }
    }
}
