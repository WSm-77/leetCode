class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        days = [0 for _ in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if temperatures[j] > temperatures[i]:
                    days[i] = j - i
                    break

        return days
    
if __name__ == "__main__":
    test = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(test.dailyTemperatures(temperatures))