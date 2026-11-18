# LeetCode 211. Design Add and Search Words Data Structure — Medium
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Submission 2198452673 — Accepted, Python3
#
# My thinking: I store the words in a trie, like
# the plain prefix tree. Searching a word with a
# dot is the same walk, except a dot tries every
# child at that level — any branch that reaches
# the end of the word as a complete word counts.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i: int) -> bool:
            if i == len(word):
                return node.is_word
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)

        return dfs(self.root, 0)
