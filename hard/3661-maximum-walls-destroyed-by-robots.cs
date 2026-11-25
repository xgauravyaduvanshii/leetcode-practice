// LeetCode 3661. Maximum Walls Destroyed by Robots — Hard
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/
// Submission 2203020961 — Accepted, C#
using System;

public class Solution {
    public int MaxWallsDestroyedByRobots(int[] robots, int[] distance, int[] walls) {
        // My thinking: sort the robots by position, then each robot
        // only ever interacts with its immediate neighbours — a shot
        // to the left is blocked by the robot on its left, a shot to
        // the right by the robot on its right, so the only walls two
        // robots can both hit are the ones between them when they
        // fire towards each other. I count, for every robot, how
        // many walls its left shot and its right shot each destroy,
        // plus the overlap between neighbours, and run a two-state
        // DP (this robot fires left / right), subtracting the
        // overlap only when neighbours fire towards each other.
        Array.Sort(robots, distance);
        Array.Sort(walls);
        int n = robots.Length;

        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            int lo = i == 0 ? robots[i] - distance[i]
                            : Math.Max(robots[i] - distance[i], robots[i - 1] + 1);
            left[i] = CountInRange(walls, lo, robots[i]);
            int hi = i == n - 1 ? robots[i] + distance[i]
                                : Math.Min(robots[i] + distance[i], robots[i + 1] - 1);
            right[i] = CountInRange(walls, robots[i], hi);
        }
        int[] overlap = new int[Math.Max(0, n - 1)];
        for (int i = 0; i < n - 1; i++) {
            overlap[i] = CountInRange(walls,
                Math.Max(robots[i + 1] - distance[i + 1], robots[i] + 1),
                Math.Min(robots[i] + distance[i], robots[i + 1] - 1));
        }
        int dpLeft = left[0], dpRight = right[0];
        for (int i = 1; i < n; i++) {
            int ndpLeft = Math.Max(dpLeft, dpRight - overlap[i - 1]) + left[i];
            int ndpRight = Math.Max(dpLeft, dpRight) + right[i];
            dpLeft = ndpLeft;
            dpRight = ndpRight;
        }
        return Math.Max(dpLeft, dpRight);
    }

    private int CountInRange(int[] w, int lo, int hi) {
        if (lo > hi) return 0;
        return UpperBound(w, hi) - LowerBound(w, lo);
    }

    private int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int UpperBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
