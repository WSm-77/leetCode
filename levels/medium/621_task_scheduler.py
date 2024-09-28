from collections import Counter, deque
from queue import PriorityQueue
import heapq

# my solution (slow)
class MySolution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        tasksCnt = Counter(tasks)
        tasksSchedule = PriorityQueue()
        cooldown = set()
        cooldownQueue = deque()
        tasksOrder = []

        time = 0

        for _ in range(n+1):
            cooldownQueue.append(None)
        for task in tasksCnt:
            tasksSchedule.put((-tasksCnt[task], task))

        while not tasksSchedule.empty():
            isNotIdleTask = True
            tmp = []
            lastPerformedTask = cooldownQueue.popleft()

            if lastPerformedTask is not None:
                cooldown.remove(lastPerformedTask)

            while not tasksSchedule.empty():
                tasksLeft, task = tasksSchedule.get()
                tasksLeft = -tasksLeft
                tmp.append([tasksLeft, task])

                if task not in cooldown:
                    isNotIdleTask = False
                    break

            if not isNotIdleTask:
                tasksLeft, task = tmp.pop()
                tasksLeft -= 1
                tasksOrder.append(task)
                cooldown.add(task)
                cooldownQueue.append(task)
                if tasksLeft > 0:
                    tasksSchedule.put((-tasksLeft, task))
            else:
                cooldownQueue.append(None)
                tasksOrder.append(None)

            for tmpTasksLeft, tmpTask in tmp:
                tasksSchedule.put((-tmpTasksLeft, tmpTask))

            time += 1

        # print(tasksOrder)

        return time

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        tasksCnt = Counter(tasks)
        cooldownQueue = deque()
        tasksOrder = []
        tasksSchedule = [(-tasksCnt[task], task) for task in tasksCnt]

        heapq.heapify(tasksSchedule)

        time = 0
        while len(tasksSchedule) > 0:
            time += 1
            tasksLeft, task = heapq.heappop(tasksSchedule)
            tasksLeft = -tasksLeft - 1

            tasksOrder.append(f"{time}: {task}")

            if tasksLeft > 0:
                cooldownQueue.append((tasksLeft, time + n, task))

            if len(cooldownQueue) == 0:
                continue

            cooldownTasksLeft, cooldownTime, cooldownTask = cooldownQueue.popleft()

            if cooldownTime == time:
                heapq.heappush(tasksSchedule, (-cooldownTasksLeft, cooldownTask))
            elif len(tasksSchedule) == 0:
                time = cooldownTime
                heapq.heappush(tasksSchedule, (-cooldownTasksLeft, cooldownTask))
            else:
                cooldownQueue.appendleft((cooldownTasksLeft, cooldownTime, cooldownTask))

        # print(tasksOrder)

        return time

if __name__ == "__main__":
    test = Solution()
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(test.leastInterval(tasks, n))
    tasks = ["A","C","A","B","D","B"]
    n = 1
    print(test.leastInterval(tasks, n))
    tasks = ["A","A","A", "B","B","B"]
    n = 3
    print(test.leastInterval(tasks, n))
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 1
    print(test.leastInterval(tasks, n))
