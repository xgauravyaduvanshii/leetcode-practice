# LeetCode 2296. Design a Text Editor — Hard
# https://leetcode.com/problems/design-a-text-editor/
# Submission 2201662839 — Accepted, Python3
#
# My thinking: the cursor is just the seam
# between two stacks — everything left of
# it in one pile, everything right of it in
# another, so every move is a handful of
# pushes and pops.

class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        deleted = 0
        while k > 0 and self.left:
            self.left.pop()
            deleted += 1
            k -= 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return ''.join(self.left[-10:])
