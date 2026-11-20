// 2621. Sleep (Easy)
// https://leetcode.com/problems/sleep/
// Submission 2200139607 -- Accepted, JavaScript
// My thinking: wrap setTimeout in a promise and await it, so the
// async function only resolves once the time has passed.
async function sleep(millis) {
    await new Promise(resolve => setTimeout(resolve, millis));
}
