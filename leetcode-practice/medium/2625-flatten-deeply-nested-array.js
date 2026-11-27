// 2625. Flatten Deeply Nested Array (Medium)
// https://leetcode.com/problems/flatten-deeply-nested-array/
// Submission 2201037848 -- Accepted, JavaScript
// My thinking: I walk the array and pull out values,
// opening nested arrays only while I still have depth
// left to spend.
var flat = function(arr, n) {
    if (n === 0) {
        return arr.slice();
    }
    const result = [];
    for (const item of arr) {
        if (Array.isArray(item)) {
            result.push(...flat(item, n - 1));
        } else {
            result.push(item);
        }
    }
    return result;
};
