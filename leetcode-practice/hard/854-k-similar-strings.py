from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # My thinking: fix the first wrong letter first — only swap
        # it with a letter that belongs there, and a swap that fixes
        # two letters at once is always worth taking right away.
        if s1 == s2:
            return 0
        queue = deque([(s1, 0)])
        seen = {s1}
        while queue:
            cur, steps = queue.popleft()
            for i in range(len(cur)):
                if cur[i] != s2[i]:
                    break
            for j in range(i + 1, len(cur)):
                if cur[j] == s2[i] and cur[j] != s2[j]:
                    nxt = list(cur)
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    nxt = "".join(nxt)
                    if nxt == s2:
                        return steps + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))
                    if cur[i] == s2[j]:
                        break
        return -1
