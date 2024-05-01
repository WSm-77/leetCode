from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []
        
        stack = deque()
        # 0 - paranthesis, 1 - opend, paranthasis, 2 - closed
        stack.append(("(", 1, 0))

        for _ in range(2*n - 2):
            newStack = deque()

            while stack:
                paranthasis, opened, closed = stack.pop()
                if opened < n:
                    newStack.append((paranthasis + "(", opened + 1, closed))

                if closed < opened:
                    newStack.append((paranthasis + ")", opened, closed + 1))
            
            stack = newStack
        
        result = []

        while stack:
            paranthasis, _, _ = stack.pop()
            result.append(paranthasis + ")")
        
        return result

if __name__ == "__main__":
    test = Solution()
    n = 3
    print(test.generateParenthesis(n))
    n = 1
    print(test.generateParenthesis(n))

