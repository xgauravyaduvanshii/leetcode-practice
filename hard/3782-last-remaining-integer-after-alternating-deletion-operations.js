// LeetCode 3782. Last Remaining Integer After Alternating Deletion Operations — Hard
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/
// Submission 2203176266 — Accepted, JavaScript
/**
 * @param {number} n
 * @return {number}
 */
var lastInteger = function(n) {
    // My thinking: the survivors always form an arithmetic
    // sequence, so I only track its first element (head),
    // its step, and how many remain. A left-to-right pass
    // keeps the odd positions, so the head never moves; a
    // right-to-left pass keeps the odd positions from the
    // right, which moves the head forward by one step
    // exactly when the count is even. Either way the count
    // halves (rounding up) and the step doubles, and the
    // passes alternate until one number is left.
    let head = 1;
    let step = 1;
    let remaining = n;
    let left = true;
    while (remaining > 1) {
        if (!left && remaining % 2 === 0) head += step;
        remaining = Math.floor((remaining + 1) / 2);
        step *= 2;
        left = !left;
    }
    return head;
};
