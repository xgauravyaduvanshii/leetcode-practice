// LeetCode 2060. Check if an Original String Exists Given Two Encoded Strings — Hard
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/
// Submission 2201565268 — Accepted, Java
//
// My thinking: I walk both encodings together
// keeping how far one side has run ahead — a
// digit pushes its side forward, a letter only
// fits when the sides are level or the letter
// can fill a wildcard the other side already
// offered.

import java.util.HashMap;
import java.util.Map;

class Solution {
    private String s1, s2;
    private Map<String, Boolean> memo = new HashMap<>();

    public boolean possiblyEquals(String s1, String s2) {
        this.s1 = s1;
        this.s2 = s2;
        return f(0, 0, 0);
    }

    private boolean f(int i, int j, int diff) {
        if (i == s1.length() && j == s2.length()) return diff == 0;
        String key = i + "," + j + "," + diff;
        if (memo.containsKey(key)) return memo.get(key);
        boolean ans = false;
        if (i < s1.length() && Character.isDigit(s1.charAt(i))) {
            int d = 0;
            for (int k = i; k < s1.length() && Character.isDigit(s1.charAt(k)); k++) {
                d = d * 10 + (s1.charAt(k) - '0');
                if (f(k + 1, j, diff + d)) {
                    ans = true;
                    break;
                }
            }
        } else if (j < s2.length() && Character.isDigit(s2.charAt(j))) {
            int d = 0;
            for (int k = j; k < s2.length() && Character.isDigit(s2.charAt(k)); k++) {
                d = d * 10 + (s2.charAt(k) - '0');
                if (f(i, k + 1, diff - d)) {
                    ans = true;
                    break;
                }
            }
        } else if (diff > 0) {
            ans = j < s2.length() && f(i, j + 1, diff - 1);
        } else if (diff < 0) {
            ans = i < s1.length() && f(i + 1, j, diff + 1);
        } else if (i < s1.length() && j < s2.length()) {
            ans = s1.charAt(i) == s2.charAt(j) && f(i + 1, j + 1, 0);
        }
        memo.put(key, ans);
        return ans;
    }
}
