class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            bit = n & 0b1
            n >>= 1
            res = res << 1 | bit

        return res

if __name__ == "__main__":
    sol = Solution()
    n = 0b00000010100101000001111010011100
    output = sol.reverseBits(n)

    assert output == 964176192
    print(output)
