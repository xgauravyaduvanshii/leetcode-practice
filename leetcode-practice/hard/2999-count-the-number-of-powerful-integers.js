// LeetCode 2999. Count the Number of Powerful Integers — Hard
// https://leetcode.com/problems/count-the-number-of-powerful-integers/
// Submission 2201864094 — Accepted, JavaScript
//
// My thinking: I count the powerful
// numbers up to a bound with a digit
// DP — the first digits may be anything
// up to the limit, the last ones must
// spell out s — then I take the count
// up to finish minus the count below
// start.

/**
 * @param {number} start
 * @param {number} finish
 * @param {number} limit
 * @param {string} s
 * @return {number}
 */
var numberOfPowerfulInt = function(start, finish, limit, s) {
  const count = (x) => {
    if (x <= 0) return 0;
    const digits = String(x);
    const n = digits.length, m = s.length;
    if (n < m) return 0;
    // Powerful numbers shorter than x: any valid prefix, then s.
    let total = 0;
    for (let len = m; len < n; len++) {
      const plen = len - m;
      total += plen === 0 ? 1 : limit * Math.pow(limit + 1, plen - 1);
    }
    // Powerful numbers with exactly n digits: walk the digits of x
    // keeping a tight flag. Free positions take 0..limit (the first
    // one 1..limit); the last m positions must match s exactly.
    let dpTight = 1, dpLoose = 0;
    for (let pos = 0; pos < n; pos++) {
      const hi = digits.charCodeAt(pos) - 48;
      let ndpTight = 0, ndpLoose = 0;
      if (pos < n - m) {
        const loD = pos === 0 ? 1 : 0;
        for (let d = loD; d <= limit; d++) {
          if (d < hi) ndpLoose += dpTight;
          else if (d === hi) ndpTight += dpTight;
        }
        ndpLoose += dpLoose * (limit + 1 - loD);
      } else {
        const d = s.charCodeAt(pos - (n - m)) - 48;
        if (d < hi) ndpLoose += dpTight;
        else if (d === hi) ndpTight += dpTight;
        ndpLoose += dpLoose;
      }
      dpTight = ndpTight;
      dpLoose = ndpLoose;
    }
    return total + dpTight + dpLoose;
  };
  return count(finish) - count(start - 1);
};
