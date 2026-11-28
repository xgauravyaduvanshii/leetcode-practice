// LeetCode 2747. Count Zero Request Servers — Medium
// https://leetcode.com/problems/count-zero-request-servers/
// Submission 2205240652 — Accepted, Java
//
// My thinking: same idea as the Python version — sort the logs
// by time, answer queries in increasing time order, and slide
// a window [q-x, q] over the logs, tracking how many servers
// have at least one request inside it.
import java.util.Arrays;

class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));
        Integer[] order = new Integer[queries.length];
        for (int i = 0; i < queries.length; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(queries[a], queries[b]));
        int[] cnt = new int[n + 1];
        int active = 0;
        int[] ans = new int[queries.length];
        int left = 0, right = 0;
        for (int qi : order) {
            int q = queries[qi];
            while (right < logs.length && logs[right][1] <= q) {
                int server = logs[right][0];
                if (cnt[server] == 0) active++;
                cnt[server]++;
                right++;
            }
            while (left < right && logs[left][1] < q - x) {
                int server = logs[left][0];
                cnt[server]--;
                if (cnt[server] == 0) active--;
                left++;
            }
            ans[qi] = n - active;
        }
        return ans;
    }
}
