// LeetCode 2007. Find Original Array From Doubled Array — Medium
// https://leetcode.com/problems/find-original-array-from-doubled-array/
// Submission 2204130876 — Accepted, Java

// My thinking: the changed array is the original array plus a doubled
// copy of every element, so an odd length can never be valid. Sort the
// array first — then the smallest unpaired number must be an original
// element, because its double is larger and cannot pair with anything
// smaller. Count how many times each value appears and walk the sorted
// values: for each value x with unpaired copies, we need the same number
// of copies of 2*x to pair with them, otherwise no original array
// exists. Zero is special because 2*0 is 0, so zeros pair with each
// other and their count must be even. Each time we pair x with 2*x, we
// add one copy of x to the answer for every unpaired copy and use up
// the matching copies of 2*x.
import java.util.*;

class Solution {
    public int[] findOriginalArray(int[] changed) {
        if (changed.length % 2 == 1) {
            return new int[0];
        }

        Map<Integer, Integer> count = new HashMap<>();
        for (int x : changed) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        List<Integer> original = new ArrayList<>();
        List<Integer> keys = new ArrayList<>(count.keySet());
        Collections.sort(keys);

        for (int x : keys) {
            int remaining = count.get(x);
            if (remaining == 0) {
                continue;
            }
            if (x == 0) {
                if (remaining % 2 == 1) {
                    return new int[0];
                }
                for (int i = 0; i < remaining / 2; i++) {
                    original.add(0);
                }
                count.put(0, 0);
                continue;
            }
            int doubles = count.getOrDefault(2 * x, 0);
            if (doubles < remaining) {
                return new int[0];
            }
            for (int i = 0; i < remaining; i++) {
                original.add(x);
            }
            count.put(2 * x, doubles - remaining);
            count.put(x, 0);
        }

        int[] ans = new int[original.size()];
        for (int i = 0; i < original.size(); i++) {
            ans[i] = original.get(i);
        }
        return ans;
    }
}
