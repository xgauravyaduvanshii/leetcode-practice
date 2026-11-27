// LeetCode 2102. Sequentially Ordinal Rank Tracker — Hard
// https://leetcode.com/problems/sequentially-ordinal-rank-tracker/
// Submission 2201574079 — Accepted, C#
//
// My thinking: the next get asks for the next
// best place, so I keep the best few in one
// heap and the rest in another — each add drops
// into the rest and swaps up if it beats the
// worst of the best, and each get pulls the
// best of the rest into the best.

public class SORTracker {
    // top: the k best so far, ordered worst-first (lowest score, then largest name).
    private readonly PriorityQueue<(int Score, string Name), (int Score, string Name)> top;
    // rest: the remaining places, ordered best-first (highest score, then smallest name).
    private readonly PriorityQueue<(int Score, string Name), (int Score, string Name)> rest;
    private int k;

    public SORTracker() {
        top = new PriorityQueue<(int, string), (int, string)>(
            Comparer<(int Score, string Name)>.Create((a, b) =>
                a.Score != b.Score ? a.Score.CompareTo(b.Score)
                                   : string.Compare(b.Name, a.Name, StringComparison.Ordinal)));
        rest = new PriorityQueue<(int, string), (int, string)>(
            Comparer<(int Score, string Name)>.Create((a, b) =>
                a.Score != b.Score ? b.Score.CompareTo(a.Score)
                                   : string.Compare(a.Name, b.Name, StringComparison.Ordinal)));
        k = 0;
    }

    public void Add(string name, int score) {
        rest.Enqueue((score, name), (score, name));
        if (top.Count > 0) {
            var worst = top.Peek();
            var best = rest.Peek();
            if (best.Score > worst.Score ||
                (best.Score == worst.Score && string.Compare(best.Name, worst.Name, StringComparison.Ordinal) < 0)) {
                rest.Dequeue();
                top.Dequeue();
                top.Enqueue(best, best);
                rest.Enqueue(worst, worst);
            }
        }
    }

    public string Get() {
        k++;
        var item = rest.Dequeue();
        top.Enqueue(item, item);
        return top.Peek().Name;
    }
}
