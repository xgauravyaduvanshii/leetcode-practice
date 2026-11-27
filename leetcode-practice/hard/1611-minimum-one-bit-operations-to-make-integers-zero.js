/**
 * @param {number} n
 * @return {number}
 */
var minimumOneBitOperations = function(n) {
    // My thinking: the top bit can only flip when the bit
    // below it is set and everything under it is clear —
    // so clear the top bit, then fix the rest backwards.
    if (n === 0) return 0;
    const k = Math.floor(Math.log2(n));
    return (1 << (k + 1)) - 1 - minimumOneBitOperations(n - (1 << k));
};
