// LeetCode 2375. Construct Smallest Number From DI String — Medium
// https://leetcode.com/problems/construct-smallest-number-from-di-string/
// Submission 2204766999 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — push the digits 1..n+1
// onto a stack and flush it at each 'I' and at the end, so every run of
// 'D's comes out reversed and the result is the smallest possible.
function smallestNumber(pattern: string): string {
    const res: string[] = [];
    const stack: string[] = [];
    const n = pattern.length;
    for (let i = 0; i <= n; i++) {
        stack.push(String(i + 1));
        if (i === n || pattern[i] === 'I') {
            while (stack.length > 0) {
                res.push(stack.pop()!);
            }
        }
    }
    return res.join('');
};
