# 入力処理
nLine = [int(i) for i in input().split()]
n = nLine[0]
m = nLine[1]
nList = [[0]*n for _ in range(n)]
for i in range(n):
    nList[i] = [int(i) for i in input().split()]

changeZeroList = [[1]*n for _ in range(n)]

# 計算処理
for i in range(n):
    for j in range(n):
        color = nList[i][j]
        if (i == 0 and nList[i+1][j] == color and (j == 0 or nList[i][j-1] == color) and (j == n-1 or nList[i][j+1] == color) and (j == 0 or nList[i+1][j-1] == color) and (j == n-1 or nList[i+1][j+1] == color)):
            changeZeroList[i][j] = 0
        if(i == n-1 and nList[i-1][j] == color and (j == 0 or nList[i][j-1] == color) and (j == n-1 or nList[i][j+1] == color) and (j == 0 or nList[i-1][j-1] == color) and (j == n-1 or nList[i-1][j+1] == color)):
            changeZeroList[i][j] = 0
        if(j == 0 and nList[i][j+1] == color and (i == 0 or nList[i-1][j] == color) and (i == n-1 or nList[i+1][j] == color) and (i == 0 or nList[i-1][j+1] == color) and (i == n-1 or nList[i+1][j+1] == color)):
            changeZeroList[i][j] = 0
        if(j == n-1 and nList[i][j-1] == color and (i == 0 or nList[i-1][j] == color) and (i == n-1 or nList[i+1][j] == color) and (i == 0 or nList[i-1][j-1] == color) and (i == n-1 or nList[i+1][j-1] == color)):
            changeZeroList[i][j] = 0

count = 0
while(count != 100):
    for i in range(1, n-1):
        for j in range(1, n-1):
            color = nList[i][j]
            if(changeZeroList[i-1][j] == 0 or changeZeroList[i+1][j] == 0 or changeZeroList[i][j-1] == 0 or changeZeroList[i][j+1] == 0):
                if((changeZeroList[i-1][j] == 0 or nList[i-1][j] == color) and (changeZeroList[i+1][j] == 0 or nList[i+1][j] == color) and (changeZeroList[i][j-1] == 0 or nList[i][j-1] == color) and (changeZeroList[i][j+1] == 0 or nList[i][j+1] == color) and (changeZeroList[i-1][j-1] == 0 or nList[i-1][j-1] == color) and (changeZeroList[i-1][j+1] == 0 or nList[i-1][j+1] == color) and (changeZeroList[i+1][j-1] == 0 or nList[i+1][j-1] == color) and (changeZeroList[i+1][j+1] == 0 or nList[i+1][j+1] == color)):
                    if(not (changeZeroList[i-1][j] == 0 and changeZeroList[i+1][j] == 0) and not (changeZeroList[i][j-1] == 0 and changeZeroList[i][j+1] == 0) and not (changeZeroList[i-1][j] == 0 and (changeZeroList[i+1][j-1] == 0 or changeZeroList[i+1][j+1] == 0)) and not (changeZeroList[i+1][j] == 0 and (changeZeroList[i-1][j-1] == 0 or changeZeroList[i-1][j+1] == 0)) and not (changeZeroList[i][j-1] == 0 and (changeZeroList[i-1][j+1] == 0 or changeZeroList[i+1][j+1] == 0)) and not (changeZeroList[i][j+1] == 0 and (changeZeroList[i-1][j-1] == 0 or changeZeroList[i+1][j-1] == 0))):
                        changeZeroList[i][j] = 0
    count += 1

while(count != 200):
    for i in range(1, n-1):
        for j in range(1, n-1):
            temp = 0
            if(changeZeroList[i-1][j] == 0):
                temp += 1
            if(changeZeroList[i+1][j] == 0):
                temp += 1
            if(changeZeroList[i][j-1] == 0):
                temp += 1
            if(changeZeroList[i][j+1] == 0):
                temp += 1
            if(temp >= 3):
                changeZeroList[i][j] = 0

    count += 1


# 反映処理
for i in range(n):
    for j in range(n):
        if(changeZeroList[i][j] == 0):
            nList[i][j] = 0


# デバック用
# print()

# 出力処理
for i in range(n):
    for j in range(n):
        print(nList[i][j], end=" ")
    print()
