// LeetCode 2398. Maximum Number of Robots Within Budget — Hard
// https://leetcode.com/problems/maximum-number-of-robots-within-budget/
// Submission 2201716868 — Accepted, TypeScript
//
// My thinking: a longer run only costs
// more, so I stretch a window as far as
// it fits and shrink it from the left when
// it breaks the budget — the widest window
// I ever hold is the answer.

function maximumRobots(chargeTimes: number[], runningCosts: number[], budget: number): number {
  const n = chargeTimes.length;
  const dq: number[] = [];
  let runSum = 0;
  let left = 0;
  let ans = 0;
  for (let right = 0; right < n; right++) {
    while (dq.length > 0 && chargeTimes[dq[dq.length - 1]] <= chargeTimes[right]) {
      dq.pop();
    }
    dq.push(right);
    runSum += runningCosts[right];
    while (dq.length > 0 && chargeTimes[dq[0]] + (right - left + 1) * runSum > budget) {
      if (dq[0] === left) dq.shift();
      runSum -= runningCosts[left];
      left++;
    }
    ans = Math.max(ans, right - left + 1);
  }
  return ans;
}
