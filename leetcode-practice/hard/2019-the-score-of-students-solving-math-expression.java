// LeetCode 2019. The Score of Students Solving Math Expression — Hard
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/
// Submission 2201319461 — Accepted, Java
//
// My thinking: the right answer earns 5, any other
// answer a wrong order of operations could still
// produce earns 2 — so I work out the right
// answer first, then every value any bracketing
// can reach, capped at 1000.

import java.util.*;

class Solution {
    public int scoreOfStudents(String s, int[] answers) {
        List<Integer> nums = new ArrayList<>();
        List<Character> ops = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            if (Character.isDigit(s.charAt(i))) {
                int j = i;
                while (j < s.length() && Character.isDigit(s.charAt(j))) j++;
                nums.add(Integer.parseInt(s.substring(i, j)));
                i = j;
            } else {
                ops.add(s.charAt(i));
                i++;
            }
        }
        // Correct answer: multiplication before addition.
        List<Integer> terms = new ArrayList<>();
        int cur = nums.get(0);
        for (int k = 0; k < ops.size(); k++) {
            if (ops.get(k) == '*') {
                cur = cur * nums.get(k + 1);
            } else {
                terms.add(cur);
                cur = nums.get(k + 1);
            }
        }
        terms.add(cur);
        int correct = 0;
        for (int t : terms) correct += t;
        // Every value any bracketing can reach, capped at 1000.
        int n = nums.size();
        Set<Integer>[][] dp = new Set[n][n];
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < n; b++) dp[a][b] = new HashSet<>();
        }
        for (int a = 0; a < n; a++) dp[a][a].add(nums.get(a));
        for (int len = 2; len <= n; len++) {
            for (int a = 0; a + len - 1 < n; a++) {
                int b = a + len - 1;
                for (int k = a; k < b; k++) {
                    for (int x : dp[a][k]) {
                        for (int y : dp[k + 1][b]) {
                            int v = ops.get(k) == '+' ? x + y : x * y;
                            if (v <= 1000) dp[a][b].add(v);
                        }
                    }
                }
            }
        }
        Set<Integer> achievable = dp[0][n - 1];
        int total = 0;
        for (int a : answers) {
            if (a == correct) total += 5;
            else if (achievable.contains(a)) total += 2;
        }
        return total;
    }
}
