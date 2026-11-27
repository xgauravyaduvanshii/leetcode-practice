// LeetCode 2405. Optimal Partition of String — Medium
// https://leetcode.com/problems/optimal-partition-of-string/
// Submission 2204786573 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — cut a new partition
// whenever the next character already appeared in the current one, so
// every partition keeps unique characters and the count is minimal.
function partitionString(s: string): number {
    const seen = new Set<string>();
    let count = 1;
    for (const ch of s) {
        if (seen.has(ch)) {
            count++;
            seen.clear();
            seen.add(ch);
        } else {
            seen.add(ch);
        }
    }
    return count;
};
