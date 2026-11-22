// LeetCode 1964. Find the Longest Valid Obstacle Course at Each Position — Hard
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
// Submission 2201274694 — Accepted, C#
//
// My thinking: I keep the smallest possible tail
// of a non-decreasing run of each length — each
// new height lands just after the equal heights,
// so it extends the longest run it can, and its
// answer is that length.

using System;
using System.Collections.Generic;

public class Solution {
    public int[] LongestObstacleCourseAtEachPosition(int[] obstacles) {
        var d = new List<int>();
        var ans = new int[obstacles.Length];
        for (int i = 0; i < obstacles.Length; i++) {
            int x = obstacles[i];
            int lo = 0, hi = d.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (d[mid] <= x) lo = mid + 1;
                else hi = mid;
            }
            if (lo == d.Count) d.Add(x);
            else d[lo] = x;
            ans[i] = lo + 1;
        }
        return ans;
    }
}
