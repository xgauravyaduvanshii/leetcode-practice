// LeetCode 2296. Design a Text Editor — Hard
// https://leetcode.com/problems/design-a-text-editor/
// Submission 2201663794 — Accepted, C#
//
// My thinking: the cursor is just the seam
// between two stacks — everything left of
// it in one pile, everything right of it in
// another, so every move is a handful of
// pushes and pops.

using System.Collections.Generic;
using System.Text;

public class TextEditor {
    private Stack<char> left = new Stack<char>();
    private Stack<char> right = new Stack<char>();

    public TextEditor() {}

    public void AddText(string text) {
        foreach (char c in text) left.Push(c);
    }

    public int DeleteText(int k) {
        int deleted = 0;
        while (k > 0 && left.Count > 0) {
            left.Pop();
            deleted++;
            k--;
        }
        return deleted;
    }

    public string CursorLeft(int k) {
        while (k > 0 && left.Count > 0) {
            right.Push(left.Pop());
            k--;
        }
        return LastLeft();
    }

    public string CursorRight(int k) {
        while (k > 0 && right.Count > 0) {
            left.Push(right.Pop());
            k--;
        }
        return LastLeft();
    }

    private string LastLeft() {
        char[] arr = left.ToArray();
        int take = System.Math.Min(10, arr.Length);
        StringBuilder sb = new StringBuilder();
        for (int i = take - 1; i >= 0; i--) sb.Append(arr[i]);
        return sb.ToString();
    }
}
