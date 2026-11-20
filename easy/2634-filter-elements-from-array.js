// 2634. Filter Elements from Array (Easy)
// https://leetcode.com/problems/filter-elements-from-array/
// Submission 2200141009 -- Accepted, JavaScript
// My thinking: build a fresh array and keep only the elements
// the test function accepts, in their original order.
var filter = function(arr, fn) {
    const filteredArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
};
