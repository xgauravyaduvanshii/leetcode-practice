function minimumMountainRemovals(nums: number[]): number {
    // My thinking: a mountain is a climb then a fall, so
    // measure the longest climb ending at each point and
    // the longest fall starting there, then join the best
    // pair at a peak.
    const n = nums.length;
    const left = new Array(n).fill(1);
    for (let i = 0; i < n; i++)
        for (let j = 0; j < i; j++)
            if (nums[j] < nums[i]) left[i] = Math.max(left[i], left[j] + 1);
    const right = new Array(n).fill(1);
    for (let i = n - 1; i >= 0; i--)
        for (let j = i + 1; j < n; j++)
            if (nums[j] < nums[i]) right[i] = Math.max(right[i], right[j] + 1);
    let best = 0;
    for (let i = 0; i < n; i++)
        if (left[i] > 1 && right[i] > 1) best = Math.max(best, left[i] + right[i] - 1);
    return n - best;
}
