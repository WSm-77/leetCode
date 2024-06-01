class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def rek(idx, currentTarget):
            nonlocal result, candidates, path, n
            if currentTarget == 0:
                result.append(path.copy())
                return
            elif currentTarget < 0 or idx == n:
                return
            
            nextDifferentNumberIdx = idx
            while nextDifferentNumberIdx < n and candidates[idx] == candidates[nextDifferentNumberIdx]:
                path.append(candidates[idx])
                nextDifferentNumberIdx += 1
            #end while

            for i in range(nextDifferentNumberIdx - idx, 0, -1):
                rek(nextDifferentNumberIdx, currentTarget - i * candidates[idx])
                path.pop()
            #end for

            rek(nextDifferentNumberIdx, currentTarget)
        #end def

        n = len(candidates)
        candidates.sort()
        result = []
        path = []
        rek(0, target)

        return result
    
if __name__ == "__main__":
    test = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(test.combinationSum2(candidates, target))
    candidates = [2,5,2,1,2]
    target = 5
    print(test.combinationSum2(candidates, target))