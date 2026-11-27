function constrainedSubsetSum(nums: number[], k: number): number {
    // My thinking: each position either starts a fresh
    // subsequence or extends the best one ending within
    // the last k positions — a sliding window keeps that
    // best in reach.
    const n = nums.length;
    const dp: number[] = new Array(n).fill(0);
    let best = -Infinity;
    const window: number[] = [];
    for (let i = 0; i < n; i++) {
        while (window.length > 0 && window[0] < i - k) window.shift();
        const prev = window.length > 0 ? dp[window[0]] : 0;
        dp[i] = nums[i] + Math.max(0, prev);
        best = Math.max(best, dp[i]);
        while (window.length > 0 && dp[window[window.length - 1]] <= dp[i]) window.pop();
        window.push(i);
    }
    return best;
}
