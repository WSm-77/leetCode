class Event:
    def __init__(self, value, isBeg):
        self.value = value
        self.isBeg = isBeg

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        events: list[Event] = []

        for beg, end in intervals:
            events.append(Event(beg, True))
            events.append(Event(end, False))

        events.sort(key=lambda event: (event.value, not event.isBeg))

        startedCnt = 0
        begVal = None

        result = []

        for event in events:
            if event.isBeg:
                if startedCnt == 0:
                    begVal = event.value
                startedCnt += 1
            else:
                startedCnt -= 1
                if startedCnt == 0:
                    result.append([begVal, event.value])

        return result

if __name__ == "__main__":
    test = Solution()

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    assert(test.merge(intervals) == [[1,6],[8,10],[15,18]])
    print(test.merge(intervals))    # expected: [[1,6],[8,10],[15,18]]

    intervals = [[1,4],[4,5]]
    assert(test.merge(intervals) == [[1,5]])
    print(test.merge(intervals))    # expected: [[1,5]]
