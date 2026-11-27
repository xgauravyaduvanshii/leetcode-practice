// 2635. Apply Transform Over Each Element in Array (Easy)
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/
// Submission 2200141500 -- Accepted, JavaScript
// My thinking: transform each element with the given function
// and collect the results in a new array, same order as input.
var map = function(arr, fn) {
    const returnedArr = [];
    for (let i = 0; i < arr.length; i++) {
        returnedArr.push(fn(arr[i], i));
    }
    return returnedArr;
};
