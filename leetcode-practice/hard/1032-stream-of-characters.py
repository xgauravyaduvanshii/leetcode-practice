class StreamChecker:
    # My thinking: store every word backwards in a trie, then
    # each new letter just walks one step deeper — a word ends
    # exactly when the walk lands on a word end.
    def __init__(self, words: list[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in reversed(word):
                node = node.setdefault(ch, {})
            node["#"] = True
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for ch in reversed(self.stream):
            if ch not in node:
                return False
            node = node[ch]
            if "#" in node:
                return True
        return False
