// LeetCode 3414. Maximum Score of Non-overlapping Intervals — Hard
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
// Submission 2202517789 — Accepted 581/581, Java
//
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public List<Integer> maximumWeight(int[][] intervals) {
        // My thinking: sort the intervals by start, so the first
        // interval after i that starts past i's end is a binary
        // search away. Then work backwards: from position i with k
        // picks left, either skip i or take it and continue from
        // that next position with k - 1 picks. Keep, for every state,
        // the best weight and — on a tie — the lexicographically
        // smallest sorted list of original indices, which is what
        // the problem asks for.
        int n = intervals.length;
        int[][] arr = new int[n][4];
        for (int i = 0; i < n; i++) {
            arr[i][0] = intervals[i][0];
            arr[i][1] = intervals[i][1];
            arr[i][2] = intervals[i][2];
            arr[i][3] = i;
        }
        Arrays.sort(arr, (a, b) -> a[0] != b[0] ? Integer.compare(a[0], b[0]) : Integer.compare(a[1], b[1]));
        int[] lefts = new int[n];
        for (int i = 0; i < n; i++) lefts[i] = arr[i][0];
        int[] nxt = new int[n];
        for (int i = 0; i < n; i++) {
            // First index whose left endpoint is past arr[i]'s end.
            int lo = 0, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (lefts[mid] <= arr[i][1]) lo = mid + 1;
                else hi = mid;
            }
            nxt[i] = lo;
        }

        // w[i][k] / sel[i][k]: best weight and sorted index list
        // using intervals from position i onward, at most k picks.
        long[][] w = new long[n + 1][5];
        List<Integer>[][] sel = new List[n + 1][5];
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k < 5; k++) sel[i][k] = new ArrayList<>();
        }
        for (int i = n - 1; i >= 0; i--) {
            int j = nxt[i];
            for (int k = 1; k < 5; k++) {
                long skipW = w[i + 1][k];
                List<Integer> skipL = sel[i + 1][k];
                long takeW = (long) arr[i][2] + w[j][k - 1];
                List<Integer> takeL = new ArrayList<>(sel[j][k - 1]);
                takeL.add(arr[i][3]);
                Collections.sort(takeL);
                if (takeW > skipW || (takeW == skipW && lexLess(takeL, skipL))) {
                    w[i][k] = takeW;
                    sel[i][k] = takeL;
                } else {
                    w[i][k] = skipW;
                    sel[i][k] = skipL;
                }
            }
        }
        return sel[0][4];
    }

    private boolean lexLess(List<Integer> a, List<Integer> b) {
        int m = Math.min(a.size(), b.size());
        for (int i = 0; i < m; i++) {
            if (!a.get(i).equals(b.get(i))) return a.get(i) < b.get(i);
        }
        return a.size() < b.size();
    }
}
