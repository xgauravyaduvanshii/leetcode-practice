public class Solution {
    public string LongestPrefix(string s) {
        // My thinking: the longest happy prefix is the longest
        // border of the string — the prefix function from the
        // Knuth-Morris-Pratt scan finds it in one pass.
        int n = s.Length;
        int[] pi = new int[n];
        for (int i = 1; i < n; i++) {
            int j = pi[i - 1];
            while (j > 0 && s[i] != s[j]) j = pi[j - 1];
            if (s[i] == s[j]) j++;
            pi[i] = j;
        }
        return s.Substring(0, pi[n - 1]);
    }
}
