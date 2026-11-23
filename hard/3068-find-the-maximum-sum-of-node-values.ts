// LeetCode 3068. Find the Maximum Sum of Node Values — Hard
// https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
// Submission 2201920269 — Accepted, TypeScript
//
// My thinking: every operation flips two
// nodes at once, so the flipped nodes
// must come in pairs — any even-sized
// set can be flipped, and no odd-sized
// set can. So I take every node where
// flipping gains value, and if that
// leaves an odd count, I give back the
// smallest gain (or take the smallest
// loss) to make the count even.

function maximumValueSum(nums: number[], k: number, edges: number[][]): number {
    let total = 0;
    for (const x of nums) total += x;
    let gainSum = 0;
    let flips = 0;
    let smallestLoss = Number.MAX_SAFE_INTEGER;
    for (const x of nums) {
        const gain = (x ^ k) - x;
        if (gain > 0) {
            gainSum += gain;
            flips++;
        }
        smallestLoss = Math.min(smallestLoss, Math.abs(gain));
    }
    if (flips % 2 === 1) gainSum -= smallestLoss;
    return total + gainSum;
}
