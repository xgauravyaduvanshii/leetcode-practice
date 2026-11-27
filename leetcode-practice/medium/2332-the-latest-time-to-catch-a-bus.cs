// LeetCode 2332. The Latest Time to Catch a Bus — Medium
// https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
// Submission 2204703988 — Accepted, C#
//
// My thinking: same idea as the Python version — sort and simulate
// boarding, then take the last bus's time if it has room, else one
// minute before the last boarded passenger, stepping down past any real
// passenger arrival time.
public class Solution {
    public int LatestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        Array.Sort(buses);
        Array.Sort(passengers);
        var pset = new HashSet<int>(passengers);
        int j = 0;
        int lastBoarded = -1;
        int boarded = 0;
        foreach (int bus in buses) {
            boarded = 0;
            while (boarded < capacity && j < passengers.Length && passengers[j] <= bus) {
                lastBoarded = passengers[j];
                j++;
                boarded++;
            }
        }
        int ans = boarded < capacity ? buses[buses.Length - 1] : lastBoarded - 1;
        while (pset.Contains(ans)) ans--;
        return ans;
    }
}
