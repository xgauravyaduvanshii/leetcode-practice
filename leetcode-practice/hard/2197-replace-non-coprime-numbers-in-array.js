// LeetCode 2197. Replace Non-Coprime Numbers in Array — Hard
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
// Submission 2201617158 — Accepted, JavaScript
//
// My thinking: neighbours that share a factor
// fuse into their lowest common multiple, and
// a fusion can wake up the pair behind it —
// so I keep a stack and fuse while the top
// two still share a factor.

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var replaceNonCoprimes = function(nums) {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    const stack = [];
    for (const x of nums) {
        stack.push(x);
        while (stack.length >= 2) {
            const a = stack[stack.length - 1];
            const b = stack[stack.length - 2];
            const g = gcd(a, b);
            if (g <= 1) break;
            stack.pop();
            stack.pop();
            stack.push(a * b / g);
        }
    }
    return stack;
};
