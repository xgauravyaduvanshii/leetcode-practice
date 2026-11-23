// LeetCode 2589. Minimum Time to Complete All Tasks — Hard
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/
// Submission 2201846755 — Accepted, JavaScript
//
// My thinking: I handle the tasks in
// the order their windows close, and
// whenever one is still short of its
// hours I switch the computer on at the
// latest free seconds inside its window
// — those late seconds are the ones the
// next tasks can still share.

/**
 * @param {number[][]} tasks
 * @return {number}
 */
var findMinimumTime = function(tasks) {
  tasks.sort((a, b) => a[1] - b[1]);
  const on = new Array(2001).fill(false);
  let total = 0;
  for (const [start, end, duration] of tasks) {
    let have = 0;
    for (let t = start; t <= end; t++) if (on[t]) have++;
    let need = duration - have;
    let t = end;
    while (need > 0 && t >= start) {
      if (!on[t]) {
        on[t] = true;
        total++;
        need--;
      }
      t--;
    }
  }
  return total;
};
