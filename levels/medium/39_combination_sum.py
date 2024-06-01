class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def rek(idx, currentTarget, elems: list[int]):
            nonlocal candidates, result

            if currentTarget == 0:
                result.append(elems)
                return
            elif idx == n or currentTarget < 0:
                return
            
            if currentTarget < candidates[idx]:
                rek(idx + 1, currentTarget, elems)
            else:
                howMany = currentTarget // candidates[idx]
                for i in range(howMany + 1):
                    rek(idx + 1, currentTarget - i * candidates[idx], elems + [candidates[idx] for _ in range(i)])

        
        result = []
        n = len(candidates)
        rek(0, target, [])
        return result
    
if __name__ == "__main__":
    test = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(test.combinationSum(candidates, target))
    candidates = [2]
    target = 1
    print(test.combinationSum(candidates, target))