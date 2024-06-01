from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        days = [0 for _ in range(n)]
        stack = deque()

        for i in range(n):
            current_temperature = temperatures[i]
            while stack and stack[-1][0] < current_temperature:
                temperature, index = stack.pop()
                days[index] = i - index
            stack.append((current_temperature, i))

        return days
    
if __name__ == "__main__":
    test = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(test.dailyTemperatures(temperatures))