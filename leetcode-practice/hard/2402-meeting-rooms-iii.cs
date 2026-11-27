// LeetCode 2402. Meeting Rooms III — Hard
// https://leetcode.com/problems/meeting-rooms-iii/
// Submission 2201720952 — Accepted, C#
//
// My thinking: a meeting takes the lowest
// free room, and if none is free it waits
// for the room that frees up first — two
// heaps keep the free rooms and the busy
// ones, and the room that hosts the most
// meetings wins.

using System;
using System.Collections.Generic;

public class Solution {
    public int MostBooked(int n, int[][] meetings) {
        Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));
        var free = new SortedSet<int>();
        for (int i = 0; i < n; i++) free.Add(i);
        var busy = new PriorityQueue<(long end, int room), (long, int)>();
        int[] counts = new int[n];
        foreach (var m in meetings) {
            long start = m[0], end = m[1];
            while (busy.Count > 0 && busy.Peek().end <= start) {
                free.Add(busy.Dequeue().room);
            }
            int room;
            if (free.Count > 0) {
                room = free.Min;
                free.Remove(room);
                busy.Enqueue((end, room), (end, room));
            } else {
                var top = busy.Dequeue();
                room = top.room;
                busy.Enqueue((top.end + end - start, room), (top.end + end - start, room));
            }
            counts[room]++;
        }
        int best = 0;
        for (int i = 1; i < n; i++) {
            if (counts[i] > counts[best]) best = i;
        }
        return best;
    }
}
