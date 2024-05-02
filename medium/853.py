from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(reverse=True)

        stack = deque()
        stack.append(cars[0])

        for i in range(1, len(cars)):
            carFleetPosition, carFleetSpeed = stack[-1]
            currentCarPosition, currentCarSpeed = cars[i]
            if Solution.getReachingTargetTime(currentCarPosition, currentCarSpeed, target) > \
                Solution.getReachingTargetTime(carFleetPosition, carFleetSpeed, target):
                stack.append((currentCarPosition, currentCarSpeed))
        

        return len(stack)

    @staticmethod
    def getReachingTargetTime(position, speed, target):
        return (target - position) / speed
    
if __name__ == "__main__":
    test = Solution()
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    print(test.carFleet(target, position, speed))
    
    target = 10
    position = [3]
    speed = [3]
    print(test.carFleet(target, position, speed))

    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    print(test.carFleet(target, position, speed))