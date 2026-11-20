// 2703. Return Length of Arguments Passed (Easy)
// https://leetcode.com/problems/return-length-of-arguments-passed/
// Submission 2200145822 -- Accepted, JavaScript
// My thinking: the rest parameter already gathers every argument
// into an array, so its length is the answer.
var argumentsLength = function(...args) {
    return args.length;
};
