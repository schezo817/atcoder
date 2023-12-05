import math
from typing import List
import sys


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Judge:
    def set_temperature(self, temperature: List[List[int]]) -> None:
        for row in temperature:
            print(" ".join(map(str, row)))
        sys.stdout.flush()

    def measure(self, i: int, y: int, x: int) -> int:
        print(f"{i} {y} {x}", flush=True)
        v = int(input())
        if v == -1:
            print(f"something went wrong. i={i} y={y} x={x}", file=sys.stderr)
            sys.exit(1)
        return v

    def answer(self, estimate: List[int]) -> None:
        print("-1 -1 -1")
        for e in estimate:
            print(e)
        sys.stdout.flush()


class Solver:

    def __init__(self, L: int, N: int, S: int, landing_pos: List[Pos]):
        self.L = L
        self.N = N
        self.S = S
        self.landing_pos = landing_pos
        self.judge = Judge()

    def solve(self) -> None:
        temperature = self._create_temperature()
        self.judge.set_temperature(temperature)
        estimate = self._predict(temperature)
        self.judge.answer(estimate)

    def _create_temperature(self) -> List[List[int]]:
        temperature = [[0] * self.L for _ in range(self.L)]
        # up_temperature = 1001 // self.N
        # 出口セルごとに気温を上げる
        for i, pos in enumerate(self.landing_pos):
            temperature[pos.y][pos.x] = min(1000, i * 10 + 1)
        temp_temp = 1
        pre_temp = 1
        # 直前の出口セルと同じ気温にする
        c = 0
        for i in range(self.L):
            for j in range(self.L):
                c += 1
                if(temperature[i][j] == 0):
                    temperature[i][j] = min(temp_temp + c, pre_temp)
                else:
                    temp_temp = temperature[i][j]
                    pre_temp = temperature[i][j]
                    c = 0
        return temperature

    def _predict(self, temperature: List[List[int]]) -> List[int]:
        estimate = [-1] * self.N
        for i_in in range(self.N):
            measured_value = 0
            measured_value_list = []
            repet = 99
            # 出口セルで繰り返し測定する
            for _ in range(repet):
                measured_value_list.append(self.judge.measure(i_in, 0, 0))
            measured_value_list.sort()
            for i in range(repet // 2 - 10, repet // 2 + 11):
                measured_value += measured_value_list[i]
            measured_value = measured_value/21
            # 一番計測値に近いセルの値を代入する
            min_diff = 9999
            for i_out, pos in enumerate(self.landing_pos):
                diff = abs(temperature[pos.y][pos.x] - measured_value)
                if diff < min_diff:
                    min_diff = diff
                    estimate[i_in] = i_out
        return estimate


def main():
    L, N, S = [int(v) for v in input().split(" ")]
    landing_pos = []
    for _ in range(N):
        y, x = (int(v) for v in input().split(" "))
        landing_pos.append(Pos(y, x))

    solver = Solver(L, N, S, landing_pos)
    solver.solve()


if __name__ == "__main__":
    main()
