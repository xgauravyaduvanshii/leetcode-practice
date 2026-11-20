/**
 * @param {number} n
 * @return {number}
 */
var numOfWays = function(n) {
    // My thinking: a row is either all three colours
    // different or the two ends the same — count both
    // kinds and step them forward row by row.
    const MOD = 1000000007;
    let abc = 6, aba = 6;
    for (let i = 1; i < n; i++) {
        const nextAbc = (2 * abc + 2 * aba) % MOD;
        const nextAba = (2 * abc + 3 * aba) % MOD;
        abc = nextAbc;
        aba = nextAba;
    }
    return (abc + aba) % MOD;
};
