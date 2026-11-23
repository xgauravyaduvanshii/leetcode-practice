// LeetCode 2081. Sum of k-Mirror Numbers — Hard
// https://leetcode.com/problems/sum-of-k-mirror-numbers/
// Submission 2201567577 — Accepted, JavaScript
//
// My thinking: a k-mirror number reads the same
// in base ten and in base k, so I build the
// base-ten palindromes in order from their first
// half and keep the ones that also mirror in
// base k, until I have enough.

/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function(k, n) {
    const isPalBaseK = (x) => {
        const digits = [];
        while (x > 0) {
            digits.push(x % k);
            x = Math.floor(x / k);
        }
        for (let i = 0, j = digits.length - 1; i < j; i++, j--) {
            if (digits[i] !== digits[j]) return false;
        }
        return true;
    };
    let total = 0;
    let found = 0;
    let length = 1;
    while (found < n) {
        const halfLen = Math.floor((length + 1) / 2);
        const start = Math.pow(10, halfLen - 1);
        const end = Math.pow(10, halfLen);
        for (let half = start; half < end; half++) {
            const s = String(half);
            let pal;
            if (length % 2 === 0) {
                pal = Number(s + s.split("").reverse().join(""));
            } else {
                pal = Number(s + s.slice(0, -1).split("").reverse().join(""));
            }
            if (isPalBaseK(pal)) {
                total += pal;
                found++;
                if (found === n) return total;
            }
        }
        length++;
    }
    return total;
};
