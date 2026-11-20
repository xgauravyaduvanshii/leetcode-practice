// 2667. Create Hello World Function (Easy)
// https://leetcode.com/problems/create-hello-world-function/
// Submission 2200144122 -- Accepted, JavaScript
// My thinking: no matter what arguments come in, the inner
// function always answers with the same greeting.
var createHelloWorld = function() {
    return function(...args) {
        return "Hello World";
    };
};
