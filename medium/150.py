from collections import deque

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = deque()
        operands = ("+", "-", "*", "/")

        for token in tokens:
            if token in operands:
                result = None
                secondNumber = stack.pop()
                firstNumber = stack.pop()

                match token:
                    case "+":
                        result = firstNumber + secondNumber
                    case "-":
                        result = firstNumber - secondNumber
                    case "*":
                        result = firstNumber * secondNumber
                    case "/":
                        result = int(firstNumber / secondNumber)

                print(f"{firstNumber} {token} {secondNumber} = {result}")
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()

if __name__ == "__main__":
    test = Solution()
    tokens = ["2","1","+","3","*"]
    print(test.evalRPN(tokens))
    tokens = ["4","13","5","/","+"]
    print()
    print(test.evalRPN(tokens))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print()
    print(test.evalRPN(tokens))