// LeetCode 2406. Divide Intervals Into Minimum Number of Groups — Medium
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
// Submission 2204789316 — Accepted, C#
//
// My thinking: same idea as the Python version — sweep +1/-1 events in
// order; the peak overlap is the number of groups needed.
public class Solution {
    public int MinGroups(int[][] intervals) {
        var events = new List<(int pos, int delta)>();
        foreach (var iv in intervals) {
            events.Add((iv[0], 1));
            events.Add((iv[1] + 1, -1));
        }
        events.Sort();
        int cur = 0;
        int ans = 0;
        foreach (var e in events) {
            cur += e.delta;
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
