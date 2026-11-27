/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function(jobDifficulty, d) {
    // My thinking: each day takes a chunk of the jobs and
    // pays its hardest job — so try every place the last
    // day could start and keep the cheapest split.
    const n = jobDifficulty.length;
    if (n < d) return -1;
    let prev = new Array(n + 1).fill(Infinity);
    prev[0] = 0;
    for (let day = 1; day <= d; day++) {
        const cur = new Array(n + 1).fill(Infinity);
        for (let i = day; i <= n; i++) {
            let hardest = 0;
            for (let j = i - 1; j >= day - 1; j--) {
                hardest = Math.max(hardest, jobDifficulty[j]);
                cur[i] = Math.min(cur[i], prev[j] + hardest);
            }
        }
        prev = cur;
    }
    return prev[n];
};
