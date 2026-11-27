class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # My thinking: build the strings one character at a time — an
        # opening bracket can always be added while fewer than n are used,
        # a closing bracket only while it would not outnumber the opening
        # ones. Every complete string of length 2n built this way is valid.
        result = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
