class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # My thinking: scan the tokens once, keeping a stack of numbers.
        # A number goes straight on the stack; an operator pops the top
        # two numbers, applies it (the first popped is the right operand),
        # and pushes the result back. Division truncates toward zero, so
        # use int(a / b) rather than //, which floors for negatives.
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]
