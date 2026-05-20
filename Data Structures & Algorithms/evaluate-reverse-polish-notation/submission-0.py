class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # token is an array of strings 
        # tokens represents a valid arithmetic expression
        # expression is in Reverse Polish Notation 

        # every time you see an operand, take out the last two elems, perform, push
        stack = []
        operators = {'+':lambda a, b: a + b, 
                    '-':lambda a, b: a - b, 
                    '*':lambda a, b: a * b, 
                    '/':lambda a, b: int(a/b)}
        for t in tokens:
            if t in operators:
                sec = stack.pop()
                first = stack.pop()
                new = operators[t](first, sec)
                stack.append(int(new))
            else:
                stack.append(int(t))
                print(stack)
        return stack[0]