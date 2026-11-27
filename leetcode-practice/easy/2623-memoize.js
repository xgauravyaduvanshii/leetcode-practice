// 2623. Memoize (Easy)
// https://leetcode.com/problems/memoize/
// Submission 2201024265 -- Accepted, JavaScript
// My thinking: I remember each call's answer in a map
// keyed by its arguments, so a repeat call just looks
// the answer up instead of computing it again.
function memoize(fn) {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
}
