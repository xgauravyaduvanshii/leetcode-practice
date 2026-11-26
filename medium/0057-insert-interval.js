// LeetCode 57. Insert Interval — Medium
// https://leetcode.com/problems/insert-interval/
// Submission 2203832952 — Accepted, JavaScript

// My thinking: I walk the intervals once, in three parts. First I copy
// every interval that ends before the new one starts. Then I merge the
// new interval with every interval it overlaps, stretching it to cover
// them all. Finally I copy the rest, which all start after the merged
// interval ends.
/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    const ans = [];
    let i = 0;
    const n = intervals.length;
    while (i < n && intervals[i][1] < newInterval[0]) {
        ans.push(intervals[i]);
        i++;
    }
    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }
    ans.push(newInterval);
    while (i < n) {
        ans.push(intervals[i]);
        i++;
    }
    return ans;
};
