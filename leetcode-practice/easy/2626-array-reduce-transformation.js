// 2626. Array Reduce Transformation (Easy)
// https://leetcode.com/problems/array-reduce-transformation/
// Submission 2200140133 -- Accepted, JavaScript
// My thinking: start from the initial value and fold the array
// left to right, feeding each element and the running value into
// the function; an empty array just returns the initial value.
var reduce = function(nums, fn, init) {
    let val = init;
    for (let i = 0; i < nums.length; i++) {
        val = fn(val, nums[i]);
    }
    return val;
};
