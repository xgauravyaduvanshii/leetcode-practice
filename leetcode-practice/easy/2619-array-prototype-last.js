// 2619. Array Prototype Last (Easy)
// https://leetcode.com/problems/array-prototype-last/
// Submission 2200138680 -- Accepted, JavaScript
// My thinking: an empty array has no last element, so return -1;
// otherwise the element at the final index is the last one.
Array.prototype.last = function() {
    if (this.length === 0) {
        return -1;
    }
    return this[this.length - 1];
};
