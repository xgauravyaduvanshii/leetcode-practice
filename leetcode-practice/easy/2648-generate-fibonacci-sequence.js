// 2648. Generate Fibonacci Sequence (Easy)
// https://leetcode.com/problems/generate-fibonacci-sequence/
// Submission 2200141927 -- Accepted, JavaScript
// My thinking: yield the current term, then roll the pair
// forward — the next term is the sum of the previous two.
var fibGenerator = function*() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
};
