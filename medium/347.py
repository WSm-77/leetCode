class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        elems = dict()

        for num in nums:
            elems[num] = 0

        for num in nums:
            elems[num] += 1

        items = list(elems.items())
        n = len(items)

        Solution.quick_select(items, 0, n - 1, k, lambda x, y: x[y][1])

        print(items)

        result = [items[i][0] for i in range(k)]

        return result
    
    def quick_select(tab, beg, end, position, key):
        while beg < end:
            pivot = Solution.partition(tab, beg, end, key)

            if pivot == position:
                return
            elif pivot < position:
                beg = pivot + 1
            else:
                end = pivot - 1

    def partition(tab, beg, end, key):
        i = beg
        for j in range(beg, end):
            if key(tab, j) >= key(tab, end):
                tab[j], tab[i] = tab[i], tab[j]
                i += 1
        
        tab[i], tab[end] = tab[end], tab[i]

        return i
    
if __name__ == "__main__":
    testTab = [1,1,1,2,2,3]
    test = Solution()
    k = 2
    print(test.topKFrequent(testTab, k))
        