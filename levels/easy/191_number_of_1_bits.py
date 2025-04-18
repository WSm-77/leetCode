class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while n > 0:
            cnt += n & 0b1
            n >>= 1

        return cnt
