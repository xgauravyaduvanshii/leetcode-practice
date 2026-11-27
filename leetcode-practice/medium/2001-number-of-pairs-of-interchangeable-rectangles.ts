// LeetCode 2001. Number of Pairs of Interchangeable Rectangles — Medium
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
// Submission 2204122575 — Accepted, TypeScript

// My thinking: two rectangles are interchangeable when their
// width-to-height ratios are equal, so I reduce each ratio to its
// simplest form by dividing both sides by their greatest common
// divisor and count how many rectangles share each reduced ratio.
// From a group of n rectangles with the same ratio, I can form
// n * (n - 1) / 2 pairs, and I add that up over all groups.
function interchangeableRectangles(rectangles: number[][]): number {
    const gcd = (a: number, b: number): number => (b === 0 ? a : gcd(b, a % b));
    const counts = new Map<string, number>();
    for (const [width, height] of rectangles) {
        const divisor = gcd(width, height);
        const key = `${width / divisor}/${height / divisor}`;
        counts.set(key, (counts.get(key) ?? 0) + 1);
    }
    let pairs = 0;
    for (const count of counts.values()) {
        pairs += (count * (count - 1)) / 2;
    }
    return pairs;
}
