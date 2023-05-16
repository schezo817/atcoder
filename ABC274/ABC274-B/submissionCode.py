import numpy as np

HW = input().split()
HList = np.zeros(int(HW[1]))

for i in range(int(HW[0])):
    WList = input()
    for j in range(int(HW[1])):
        if(WList[j] == "#"):
            HList[j] += 1

for i in range(HList.size):
    print(int(HList[i]), end=" ")
