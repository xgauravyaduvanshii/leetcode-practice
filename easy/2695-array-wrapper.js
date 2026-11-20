// 2695. Array Wrapper (Easy)
// https://leetcode.com/problems/array-wrapper/
// Submission 2200145229 -- Accepted, JavaScript
// My thinking: store the numbers on the object; valueOf adds them
// up so + works, toString joins them in brackets like JSON.
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((sum, n) => sum + n, 0);
};

ArrayWrapper.prototype.toString = function() {
    return "[" + this.nums.join(",") + "]";
};
