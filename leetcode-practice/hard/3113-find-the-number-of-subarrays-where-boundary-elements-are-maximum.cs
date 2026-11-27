// LeetCode 3113. Find the Number of Subarrays Where Boundary Elements Are Maximum — Hard
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
// Submission 2202002248 — Accepted, C#
//
// My thinking: I sweep the numbers with
// a decreasing stack that remembers, for
// each distinct value, how many equal
// values in a row sit on top. A new
// number pops everything smaller, then
// either extends the run of equals —
// every subarray ending here whose
// boundary is that value counts — or
// starts a new run with just itself.

public class Solution {
    public long NumberOfSubarrays(int[] nums) {
        var stack = new Stack<(int val, long cnt)>();
        long ans = 0;
        foreach (int x in nums) {
            while (stack.Count > 0 && stack.Peek().val < x) stack.Pop();
            if (stack.Count > 0 && stack.Peek().val == x) {
                ans += stack.Peek().cnt + 1;
                var t = stack.Pop();
                stack.Push((x, t.cnt + 1));
            } else {
                ans += 1;
                stack.Push((x, 1));
            }
        }
        return ans;
    }
}
