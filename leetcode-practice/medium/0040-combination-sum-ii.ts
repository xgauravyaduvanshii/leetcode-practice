// LeetCode 40. Combination Sum II — Medium
// https://leetcode.com/problems/combination-sum-ii/
// Submission 2203822513 — Accepted, TypeScript

// My thinking: like Combination Sum, I build combinations with
// backtracking, but each candidate may be used only once, so after
// taking a number I move to the next index. I sort first and skip a
// candidate when it equals the previous one at the same level, which
// keeps duplicate combinations out of the answer.
function combinationSum2(candidates: number[], target: number): number[][] {
    candidates.sort((a, b) => a - b);
    const ans: number[][] = [];
    const combo: number[] = [];

    function backtrack(start: number, remaining: number): void {
        if (remaining === 0) {
            ans.push([...combo]);
            return;
        }
        if (remaining < 0) return;
        for (let i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] === candidates[i - 1]) continue;
            combo.push(candidates[i]);
            backtrack(i + 1, remaining - candidates[i]);
            combo.pop();
        }
    }

    backtrack(0, target);
    return ans;
}
