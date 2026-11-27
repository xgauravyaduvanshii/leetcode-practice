// LeetCode 2358. Maximum Number of Groups Entering a Competition — Medium
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
// Submission 2204738470 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — only the student count
// matters, so take the largest k with 1+2+...+k <= n.
function maximumGroups(grades: number[]): number {
    const n = grades.length;
    let k = 0;
    let total = 0;
    while (total + k + 1 <= n) {
        k++;
        total += k;
    }
    return k;
};
