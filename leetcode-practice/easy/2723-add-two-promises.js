// 2723. Add Two Promises (Easy)
// https://leetcode.com/problems/add-two-promises/
// Submission 2200147494 -- Accepted, JavaScript
// My thinking: wait for both promises to settle, then add the
// two resolved values together.
var addTwoPromises = async function(promise1, promise2) {
    const [a, b] = await Promise.all([promise1, promise2]);
    return a + b;
};
