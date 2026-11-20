// 2629. Function Composition (Easy)
// https://leetcode.com/problems/function-composition/
// Submission 2200140625 -- Accepted, JavaScript
// My thinking: composition applies the last function first, so
// walk the list backwards; with no functions the input passes
// through unchanged.
var compose = function(functions) {
    return function(x) {
        let result = x;
        for (let i = functions.length - 1; i >= 0; i--) {
            result = functions[i](result);
        }
        return result;
    };
};
