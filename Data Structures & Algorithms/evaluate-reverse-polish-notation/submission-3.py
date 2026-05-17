class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"

        for element in tokens:
            if element not in operators:
                stack.append(int(element))
            else:
                first = stack.pop()
                second = stack.pop()
                if element == "+":
                    res = first + second
                    stack.append(res)

                elif element == "-":
                    res = second - first
                    stack.append(res)
                
                elif element == "*":
                    res = second * first
                    stack.append(res)

                else:
                    res = int(second / first)
                    stack.append(res)

        return stack[0]