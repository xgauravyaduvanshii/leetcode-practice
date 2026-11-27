public class Solution {
    public int DistinctEchoSubstrings(string text) {
        // My thinking: an echo substring is two identical halves
        // back to back — try every split point and grow the
        // halves together, keeping the ones we have seen.
        int n = text.Length;
        var seen = new HashSet<string>();
        for (int mid = 1; mid < n; mid++) {
            int length = 1;
            while (mid - length >= 0 && mid + length - 1 < n) {
                string left = text.Substring(mid - length, length);
                string right = text.Substring(mid, length);
                if (left == right) {
                    seen.Add(left + right);
                }
                length++;
            }
        }
        return seen.Count;
    }
}
