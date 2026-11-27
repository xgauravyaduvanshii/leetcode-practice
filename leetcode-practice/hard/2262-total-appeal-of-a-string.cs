// LeetCode 2262. Total Appeal of A String — Hard
// https://leetcode.com/problems/total-appeal-of-a-string/
// Submission 2201642854 — Accepted, C#
//
// My thinking: a letter only adds to the
// substrings ending here when it has not
// shown up since the substring began — so
// each position adds exactly the gap back
// to its last sighting.

using System.Collections.Generic;

public class Solution {
    public long AppealSum(string s) {
        var last = new Dictionary<char, int>();
        long dp = 0;
        long total = 0;
        for (int i = 0; i < s.Length; i++) {
            int prev = last.TryGetValue(s[i], out int p) ? p : -1;
            dp += i - prev;
            total += dp;
            last[s[i]] = i;
        }
        return total;
    }
}
