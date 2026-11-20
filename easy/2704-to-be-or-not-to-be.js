// 2704. To Be Or Not To Be (Easy)
// https://leetcode.com/problems/to-be-or-not-to-be/
// Submission 2200146341 -- Accepted, JavaScript
// My thinking: each check either passes quietly with true or
// throws the exact error message the tests expect.
var expect = function(val) {
    return {
        toBe: function(other) {
            if (val !== other) {
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe: function(other) {
            if (val === other) {
                throw new Error("Equal");
            }
            return true;
        }
    };
};
