class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # My thinking: read the string like a tiny grammar — each
        # operator wraps a list of sub-expressions, and the stack
        # folds them up as the closing brackets arrive.
        stack = []
        for ch in expression:
            if ch in "tf!&|":
                stack.append(ch)
            elif ch == ")":
                values = []
                while stack[-1] != "(":
                    values.append(stack.pop() == "t")
                stack.pop()  # '('
                op = stack.pop()
                if op == "!":
                    stack.append("t" if not values[0] else "f")
                elif op == "&":
                    stack.append("t" if all(values) else "f")
                else:
                    stack.append("t" if any(values) else "f")
            elif ch == "(":
                stack.append(ch)
        return stack[0] == "t"
