// 2724. Sort By (Easy)
// https://leetcode.com/problems/sort-by/
// Submission 2200148055 -- Accepted, JavaScript
// My thinking: compare two elements by their fn values — the
// smaller fn value comes first.
var sortBy = function(arr, fn) {
    return arr.sort((a, b) => fn(a) - fn(b));
};
