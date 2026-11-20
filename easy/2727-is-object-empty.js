// 2727. Is Object Empty (Easy)
// https://leetcode.com/problems/is-object-empty/
// Submission 2200150159 -- Accepted, JavaScript
// My thinking: an object or array is empty when it has no keys
// at all, so count the keys and check for zero.
var isEmpty = function(obj) {
    return Object.keys(obj).length === 0;
};
