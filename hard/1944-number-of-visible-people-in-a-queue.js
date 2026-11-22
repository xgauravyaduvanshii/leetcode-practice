// LeetCode 1944. Number of Visible People in a Queue — Hard
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/
// Submission 2201255532 — Accepted, JavaScript
//
// My thinking: scan from right to left with a strictly decreasing stack of
// heights. Each person sees every shorter person on the stack until the
// first taller-or-equal one, which they also see — then that taller person
// blocks the view of everyone behind them. An equal-height person is seen
// but then leaves the stack, because the nearer equal height hides it
// from everyone further left.

function canSeePersonsCount(heights) {
    const n = heights.length;
    const answer = new Array(n).fill(0);
    const stack = [];
    for (let i = n - 1; i >= 0; i--) {
        let count = 0;
        while (stack.length > 0 && heights[i] > stack[stack.length - 1]) {
            stack.pop();
            count++;
        }
        if (stack.length > 0) {
            count++;
            if (stack[stack.length - 1] === heights[i]) stack.pop();
        }
        answer[i] = count;
        stack.push(heights[i]);
    }
    return answer;
}
