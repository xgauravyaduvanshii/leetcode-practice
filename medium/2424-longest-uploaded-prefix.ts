// LeetCode 2424. Longest Uploaded Prefix — Medium
// https://leetcode.com/problems/longest-uploaded-prefix/
// Submission 2204861690 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — a set of uploaded
// videos plus a pointer that only moves forward while the next video
// is already uploaded.
class LUPrefix {
    private seen: Set<number>;
    private cur: number;
    constructor(n: number) {
        this.seen = new Set<number>();
        this.cur = 0;
    }
    upload(video: number): void {
        this.seen.add(video);
    }
    longest(): number {
        while (this.seen.has(this.cur + 1)) {
            this.cur++;
        }
        return this.cur;
    }
}
