from collections import defaultdict
from typing import List

class DetectSquares:
    def __init__(self):
        self.coord = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.coord[x][y] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        point_x, point_y = point

        for y in self.coord[point_x]:
            if y == point_y:
                continue

            size = y - point_y

            x1 = point_x + size
            x2 = point_x - size

            res += self.coord[x1][point_y] * self.coord[x1][y] * self.coord[point_x][y]
            res += self.coord[x2][point_y] * self.coord[x2][y] * self.coord[point_x][y]

        return res

def test(commands, input_command, expected_output):
    obj = DetectSquares()
    for cmd, inp, exp_out in zip(commands, input_command, expected_output):
        if cmd == "add":
            out = obj.add(*inp)
        elif cmd == "count":
            out = obj.count(*inp)

        print(f"output: {out}, expected: {exp_out}")

if __name__ == "__main__":
    sol = DetectSquares()
    cmds = ["add", "add", "add", "count", "count", "add", "count"]
    inpts = [[[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    outpts = [None, None, None, 1, 0, None, 2]

    test(cmds, inpts, outpts)
