// LeetCode 2376. Count Special Integers — Hard
// https://leetcode.com/problems/count-special-integers/
// Submission 2201703406 — Accepted, Java
//
// My thinking: shorter numbers are counted
// by choosing distinct digits, and numbers
// as long as n are counted digit by digit
// — at each step I may pick any unused
// digit below n's, then fill the rest
// freely from what is left.

class Solution {
    public int countSpecialNumbers(int n) {
        String s = String.valueOf(n);
        int L = s.length();
        int ans = 0;
        for (int length = 1; length < L; length++) {
            int count = 9;
            int avail = 9;
            for (int i = 1; i < length; i++) {
                count *= avail;
                avail--;
            }
            ans += count;
        }
        boolean[] used = new boolean[10];
        for (int i = 0; i < L; i++) {
            int d = s.charAt(i) - '0';
            int remaining = L - i - 1;
            int start = i == 0 ? 1 : 0;
            for (int smaller = start; smaller < d; smaller++) {
                if (used[smaller]) continue;
                int count = 1;
                int avail = 10 - i - 1;
                for (int j = 0; j < remaining; j++) {
                    count *= avail;
                    avail--;
                }
                ans += count;
            }
            if (used[d]) return ans;
            used[d] = true;
        }
        ans += 1;
        return ans;
    }
}
