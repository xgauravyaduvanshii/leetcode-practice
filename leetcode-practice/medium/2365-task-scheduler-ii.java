// LeetCode 2365. Task Scheduler II — Medium
// https://leetcode.com/problems/task-scheduler-ii/
// Submission 2204749626 — Accepted, Java
//
// My thinking: same idea as the Python version — remember the last day
// each task type ran, wait until last + space + 1 when a repeat comes
// too soon, and count the days. Longs are used because the day count
// can exceed 32 bits.
class Solution {
    public long taskSchedulerII(int[] tasks, int space) {
        java.util.Map<Integer, Long> last = new java.util.HashMap<>();
        long day = 0;
        for (int t: tasks) {
            Long prev = last.get(t);
            if (prev != null) {
                day = Math.max(day, prev + space + 1);
            }
            last.put(t, day);
            day++;
        }
        return day;
    }
}
